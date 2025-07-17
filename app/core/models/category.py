from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey

from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime, timezone
from .mixins import IntIdPkMixin
from .mixins.created_at import CreatedAtMixin

if TYPE_CHECKING:
    from core.models.product import Product

class Category(CreatedAtMixin, IntIdPkMixin, Base):
    __tablename__ = "categories"
    name: Mapped[str]
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