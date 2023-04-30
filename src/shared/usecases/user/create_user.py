from injector import inject
from src.shared.interfaces.repositories.user_repository import UserRepositoryABC
from src.shared.interfaces.usecases.user.create_user import CreateUserUsecaseABC
from src.shared.interfaces.usecases.user.create_user_input_data import CreateUserInputData


class CreateUserUsecase(CreateUserUsecaseABC):
    @inject
    def __init__(self, repository: UserRepositoryABC) -> None:
        self.__repository = repository
    
    def handle(self, input_data: CreateUserInputData):
        pass
