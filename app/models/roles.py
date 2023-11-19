import sqlalchemy as sa
from sqlalchemy.orm import relationship

from db.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    permissions = sa.Column(sa.JSON)
    users = relationship("User", back_populates="role", lazy="selectin")
