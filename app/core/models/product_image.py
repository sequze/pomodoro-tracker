from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .base import Base
from .mixins import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin

if TYPE_CHECKING:
    from .product import Product

class ProductImage(CreatedAtMixin, IntIdPkMixin, Base):
    url: Mapped[str]
    alt_text: Mapped[str]
    is_main: Mapped[bool]
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="images")
