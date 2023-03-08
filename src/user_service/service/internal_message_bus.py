from typing import Dict, Union, Callable, List, Type
from domains import commands, events
import logging

from service import unit_of_work

Message = Union[commands.Command, events.Event]


class MessageBus:
    def __init__(
        self,
        config: Dict,
        uow: unit_of_work.UnitOfWork,
        command_handlers: Dict[Type[events.Event], Callable],
        event_handlers: Dict[Type[events.Event], List[Callable]],
    ):
        self.config = config
        self.uow = uow
        self.command_handlers = command_handlers
        self.event_handlers = event_handlers

    def handle(self, message: Message):
        self.queue = [message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, commands.commands):
                self.handle_command(message)
            elif isinstance(message, events.Event):
                self.handle_event(message)
            else:
                raise TypeError(message)

    def handle_command(self, command: Type[commands.Command]):
        logging.debug("Handling command %s", command)
        try:
            handler = self.command_handlers[type(command)]
            handler(command)
            self.queue.extend(self.uow.collect_new_events())
        except Exception:
            logging.exception("Exception while handling command %s", command)
            raise

    def handle_event(self, event: Type[events.Event]):
        logging.debug("Handling event %s", event)
        try:
            handler = self.event_handlers[type(event)]
            handler(event)
            self.queue.extend(self.uow.collect_new_events())
        except Exception:
            logging.exception("Exception while handling command %s", event)
            raise
