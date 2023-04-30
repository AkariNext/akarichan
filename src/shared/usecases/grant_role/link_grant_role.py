from injector import inject
from src.shared.interfaces.repositories.grant_role_repository import GrantRoleRepositoryABC
from src.shared.interfaces.usecases.grant_role.link_grant_role import LinkGrantRoleUsecaseABC
from src.shared.interfaces.usecases.grant_role.link_grant_role_input_data import LinkGrantRoleInputData


class LinkGrantRoleUsecase(LinkGrantRoleUsecaseABC):
    @inject
    def __init__(self, repository: GrantRoleRepositoryABC) -> None:
        self.__repository: GrantRoleRepositoryABC = repository
    
    async def handle(self, input_data: LinkGrantRoleInputData) -> None:
        await self.__repository.link(**input_data)