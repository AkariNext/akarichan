from abc import ABC, abstractmethod


class GrantRoleRepositoryABC(ABC):
    @abstractmethod
    async def link(self,  guild_id: str, emoji: str, role_id: str) -> None:
        pass
