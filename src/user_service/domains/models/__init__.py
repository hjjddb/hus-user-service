import uuid
from datetime import datetime


class Model:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_time = datetime.utcnow()
        self.updated_time = datetime.utcnow()
