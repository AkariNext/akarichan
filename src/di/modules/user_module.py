
from injector import Binder, Module

from src.shared.domain.user.user_repository import UserRepository
from src.shared.interfaces.repositories.user_repository import UserRepositoryABC
from src.shared.interfaces.usecases.user.create_user import CreateUserUsecaseABC
from src.shared.usecases.user.create_user import CreateUserUsecase


class UserModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(UserRepositoryABC, UserRepository)
        binder.bind(CreateUserUsecaseABC, CreateUserUsecase)
