from typing import TypedDict


class LinkGrantRoleInputData(TypedDict):
    guild_id: int
    emoji: str
    role_id: str