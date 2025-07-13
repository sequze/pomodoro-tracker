from enum import Enum

from .base import Base
from .mixins import IntIdPkMixin
from datetime import datetime, timezone

class UserRole(str, Enum):
    customer="customer"
    admin="admin"


from sqlalchemy.orm import Mapped, mapped_column
class User(IntIdPkMixin, Base):
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str]
    role: Mapped[UserRole] = mapped_column(default=UserRole.customer)
    created_at: Mapped[datetime] = mapped_column(
        default_factory=lambda: datetime.now(timezone.utc))