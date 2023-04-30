from injector import Injector

from src.di.modules.user_module import UserModule

di_container = Injector([UserModule])


