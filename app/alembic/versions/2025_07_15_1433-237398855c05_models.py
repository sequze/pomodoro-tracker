"""models

Revision ID: 237398855c05
Revises: 
Create Date: 2025-07-15 14:33:28.126854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '237398855c05'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('categories',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], name=op.f('fk_categories_parent_id_categories')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_categories'))
    )
    op.create_table('discounts',
    sa.Column('percent', sa.Float(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.CheckConstraint('percent > 0 AND percent <= 100', name=op.f('ck_discounts_percent_range')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_discounts'))
    )
    op.create_table('users',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('customer', 'admin', name='userrole'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    op.create_table('orders',
    sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('status', sa.Enum('pending', 'paid', 'processing', 'shipped', 'delivered', 'completed', 'cancelled', 'refunded', name='orderstatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_orders_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    op.create_table('products',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_products_category_id_categories')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_products'))
    )
    op.create_table('cartitems',
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_cartitems_product_id_products')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_cartitems_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cartitems'))
    )
    op.create_table('orderitems',
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_orderitems_order_id_orders')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_orderitems_product_id_products')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orderitems'))
    )
    op.create_table('product_discount_association',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('discount_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discount_id'], ['discounts.id'], name=op.f('fk_product_discount_association_discount_id_discounts')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_product_discount_association_product_id_products')),
    sa.PrimaryKeyConstraint('product_id', 'discount_id', name=op.f('pk_product_discount_association'))
    )
    op.create_table('productimages',
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('alt_text', sa.String(), nullable=False),
    sa.Column('is_main', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_productimages_product_id_products')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_productimages'))
    )


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productimages')
    op.drop_table('product_discount_association')
    op.drop_table('orderitems')
    op.drop_table('cartitems')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('users')
    op.drop_table('discounts')
    op.drop_table('categories')
    # ### end Alembic commands ###
