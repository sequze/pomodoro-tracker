from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .base import Base
from .mixins import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin
from .product_discount_association_table import product_discount_association_table

if TYPE_CHECKING:
    from .category import Category
    from .product_image import ProductImage
    from .discount import Discount

class Product(CreatedAtMixin, IntIdPkMixin, Base):
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    # relationships
    category: Mapped["Category"] = relationship(back_populates="products")
    images: Mapped[list["ProductImage"]] = relationship(back_populates="product")
    discounts: Mapped[list["Discount"]] = relationship(
        secondary=product_discount_association_table,
        back_populates="products",
    )