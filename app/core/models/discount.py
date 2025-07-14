from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .base import Base
from .mixins import IntIdPkMixin
from .product_discount_association_table import product_discount_association_table
if TYPE_CHECKING:
    from .product import Product


class Discount(IntIdPkMixin, Base):
    percent: Mapped[float] = mapped_column()
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    description: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    products: Mapped[list["Product"]] = relationship(
        secondary=product_discount_association_table,
        back_populates="discounts",
    )
    __table_args__ = (
        CheckConstraint('percent > 0 AND percent <= 100', name='percent_range'),
    )
