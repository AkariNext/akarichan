import uuid
from sqlmodel import SQLModel, Field


class GrantRole(SQLModel, table=True):
    id: str = Field(default=str(uuid.uuid4()), primary_key=True)
    role_id: int
    emoji_id: int
    guild_id: int
    
    