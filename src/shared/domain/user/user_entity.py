from datetime import datetime
import uuid
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: str = Field(default=uuid.uuid4(), primary_key=True)
    name: str
    created_at: datetime = Field(default=datetime.utcnow())

