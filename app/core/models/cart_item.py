from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .base import Base
from .mixins import IntIdPkMixin, CreatedAtMixin

if TYPE_CHECKING:
    from .user import User
    from .product import Product

class CartItem(IntIdPkMixin, CreatedAtMixin, Base):
    quantity: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    user: Mapped["User"] = relationship(back_populates="cart_items")
    product: Mapped["Product"] = relationship()