import uuid
from sqlmodel import SQLModel, Field


class GrantRole(SQLModel, table=True):
    id: str = Field(default=uuid.uuid4(), primary_key=True)
    role_id: str
    emoji: str
    guild_id: str
    
    