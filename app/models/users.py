import enum

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Faculties(str, enum.Enum):
    bio = "Биологический факультет"
    war = "Военный факультет"
    geo = "Факультет географии и геоинформатики"
    journ = "Факультет журналистики"
    hist = "Исторический факультет"
    mech = "Механико-математический факультет"
    famcs = "Факультет прикладной математики и информатики"
    raf = "Факульет радиофизики и компьютерных технологий"
    soc_comm = "Факультет социокультурных коммуникаций"
    fil_soc = "Факультет философии и социальных наук"
    fiz = "Физический факультет"
    fil = "Филологический факультет"
    chem = "Химический факультет"
    econ = "Экономический факультет"
    law = "Юридический факультет"
    rel = "Факультет международных отношений"

    buis = "Институт бизнеса"
    eco = "Экологический институт"
    teo = "Институт теологии"
    chin = "Институт китаеведения"
    lyc = "Лицей БГУ"
    col = "Юридичекий колледж БГУ"


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    surname = sa.Column(sa.String, nullable=False)
    patronymic = sa.Column(sa.String)
    photo = sa.Column(sa.String)
    faculty = sa.Column(sa.Enum(Faculties), default=Faculties.famcs)
    course = sa.Column(sa.Integer)
    group = sa.Column(sa.String)
    email = sa.Column(sa.String)
    telegram = sa.Column(sa.String)
    login = sa.Column(sa.String, nullable=False, unique=True)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    role = relationship("Role", back_populates="users", lazy="selectin")
    role_id = sa.Column(sa.Integer, ForeignKey("roles.id"))
