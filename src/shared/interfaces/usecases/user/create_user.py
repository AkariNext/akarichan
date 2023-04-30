from abc import ABC, abstractmethod

from src.shared.interfaces.repositories.user_repository import UserRepositoryABC
from src.shared.interfaces.usecases.user.create_user_input_data import CreateUserInputData


class CreateUserUsecaseABC(ABC):
    @abstractmethod
    def __init__(self, repository: UserRepositoryABC) -> None:
        pass
    
    @abstractmethod
    def handle(self, input_data: CreateUserInputData):
        pass
