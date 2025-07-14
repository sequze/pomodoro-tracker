from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .mixins import IntIdPkMixin

if TYPE_CHECKING:
    from core.models.product import Product

class Category(IntIdPkMixin, Base):
    __tablename__ = "categories"
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc))
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True)

    parent: Mapped["Category"] = relationship(
        back_populates="children",
        remote_side="Category.id",
        uselist=False,
    )
    children: Mapped[list["Category"]] = relationship(back_populates="parent")