from enum import Enum
from typing import TYPE_CHECKING

from .base import Base
from .mixins import IntIdPkMixin
from datetime import datetime, timezone

from .mixins.created_at import CreatedAtMixin


class UserRole(str, Enum):
    customer="customer"
    admin="admin"

if TYPE_CHECKING:
    from .cart_item import CartItem
    from .order import Order
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(CreatedAtMixin, IntIdPkMixin, Base):
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    full_name: Mapped[str]
    role: Mapped[UserRole] = mapped_column(default=UserRole.customer)
    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="user")
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User {self.full_name}, id: {self.id} email: {self.email}, created at: {self.created_at}"