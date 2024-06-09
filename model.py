from pydantic import BaseModel
from datetime import datetime


class Todo(BaseModel):
    id : str
    item : str
    timestamp: datetime