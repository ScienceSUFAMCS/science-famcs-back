from pydantic import BaseModel
from pydantic.fields import Any

from app.models.roles import Role


class JSONForm(BaseModel):
    id: int
    name: str
    permissions: Any

    @classmethod
    def custom_init(cls, role: Role):
        return cls(id=role.id, name=role.name, permissions=role.permissions)
