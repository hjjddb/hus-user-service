import dataclasses
from domains import Message


@dataclasses.dataclass(init=False)
class Command(Message):
    def __init__(self):
        super().__init__(self)


@dataclasses.dataclass
class CreateUserCommand(Command):
    username: str
    password: str
    email: str
    name: str
