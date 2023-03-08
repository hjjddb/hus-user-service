import dataclasses
import uuid
from datetime import datetime


@dataclasses.dataclass(init=False)
class Message:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_time = datetime.utcnow()
        self.updated_time = self.created_time
