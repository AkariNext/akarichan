from injector import Injector
from src.di.modules.grant_role_module import GrantRoleModule

from src.di.modules.user_module import UserModule

di_container = Injector([UserModule, GrantRoleModule])


