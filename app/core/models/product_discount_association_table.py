from sqlalchemy import Table, Column, ForeignKey

from .base import Base

product_discount_association_table = Table(
    "product_discount_association",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("discount_id", ForeignKey("discounts.id"), primary_key=True),
)
