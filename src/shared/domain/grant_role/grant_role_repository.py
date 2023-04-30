from sqlmodel import Session

from src.shared.infrastructure.database import engine
from src.shared.domain.grant_role.grant_role_entity import GrantRole
from src.shared.interfaces.repositories.grant_role_repository import GrantRoleRepositoryABC


class GrantRoleRepository(GrantRoleRepositoryABC):
    async def link(self, guild_id: str, emoji: str, role_id: str) -> None:
        new_grant_role = GrantRole(role_id=role_id, emoji=emoji, guild_id=guild_id)
        with Session(engine) as session:
            session.add(new_grant_role)
            session.commit()
        
    