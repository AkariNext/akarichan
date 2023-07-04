from abc import ABC, abstractmethod

from shared.infrastructure.database import prisma

class IUserService(ABC):
    @abstractmethod
    async def create(self, discord_user_id: str):
        prisma