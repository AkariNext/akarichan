from injector import Binder, Module
from src.shared.domain.grant_role.grant_role_repository import GrantRoleRepository

from src.shared.interfaces.repositories.grant_role_repository import GrantRoleRepositoryABC
from src.shared.interfaces.usecases.grant_role.link_grant_role import LinkGrantRoleUsecaseABC
from src.shared.usecases.grant_role.link_grant_role import LinkGrantRoleUsecase


class GrantRoleModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(GrantRoleRepositoryABC, GrantRoleRepository)
        binder.bind(LinkGrantRoleUsecaseABC, LinkGrantRoleUsecase)
