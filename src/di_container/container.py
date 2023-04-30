from injector import Injector

from src.di_container.modules.user_module import UserModule

di_container = Injector([UserModule])


