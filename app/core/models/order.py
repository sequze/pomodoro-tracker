from typing import TYPE_CHECKING

from sqlalchemy import Numeric, ForeignKey
from decimal import Decimal
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .base import Base
from .mixins import IntIdPkMixin
from enum import Enum

if TYPE_CHECKING:
    from .user import User
    from .order_item import OrderItem

VALID_TRANSITIONS = {
    "pending": {"paid", "cancelled"}, # cancelled может делать пользователь
    "paid": {"processing", "shipped", "cancelled", "refunded"},
    "processing": {"shipped", "cancelled"},
    "shipped": {"delivered", "refunded"},
    "delivered": {"completed", "refunded"},
    "completed": set(),
    "cancelled": set(),
    "refunded": set(),
}

class OrderStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    completed = "completed"
    cancelled = "cancelled"
    refunded = "refunded"

class Order(IntIdPkMixin, Base):
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[OrderStatus]
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship(back_populates="order")