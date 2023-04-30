from abc import ABC, abstractmethod


class GrantRoleRepositoryABC(ABC):
    @abstractmethod
    async def link(self,  guild_id: int, emoji_id: int, role_id: int) -> None:
        pass
