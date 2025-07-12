from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import MetaData
from core.config import settings

class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    __abstract__ = True
    metadata = MetaData(naming_convention=settings.db.naming_convention)

