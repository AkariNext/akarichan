from abc import ABC, abstractmethod
from src.shared.interfaces.repositories.grant_role_repository import GrantRoleRepositoryABC

from src.shared.interfaces.usecases.grant_role.link_grant_role_input_data import LinkGrantRoleInputData


class LinkGrantRoleUsecaseABC(ABC):
    @abstractmethod
    def __init__(self, repository: GrantRoleRepositoryABC) -> None:
        pass
    
    @abstractmethod
    async def handle(self, input_data: LinkGrantRoleInputData) -> None:
        pass
