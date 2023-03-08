import dataclasses
from domains import Message


@dataclasses.dataclass(init=False)
class Event(Message):
    def __init__(self):
        super().__init__()
