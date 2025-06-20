"""delete tables

Revision ID: 2287fab97d24
Revises: 122d51331920
Create Date: 2025-06-19 01:16:56.139248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2287fab97d24'
down_revision: Union[str, None] = '122d51331920'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_orders_id', table_name='orders')
    op.drop_table('orders')
    op.drop_index('ix_customers_id', table_name='customers')
    op.drop_table('customers')
    op.drop_index('ix_addresses_id', table_name='addresses')
    op.drop_table('addresses')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('addresses_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('city', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('address_line_1', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('address_line_2', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('postcode', sa.VARCHAR(length=7), autoincrement=False, nullable=False),
    sa.Column('delivery_instructions', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='addresses_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_addresses_id', 'addresses', ['id'], unique=False)
    op.create_table('customers',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('customers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.VARCHAR(length=36), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='customers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_customers_id', 'customers', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('scheduled_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('picked_up_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('delivered_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('pickup_address_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('delivery_address_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='orders_customer_id_fkey'),
    sa.ForeignKeyConstraint(['delivery_address_id'], ['addresses.id'], name='orders_delivery_address_id_fkey'),
    sa.ForeignKeyConstraint(['pickup_address_id'], ['addresses.id'], name='orders_pickup_address_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='orders_pkey')
    )
    op.create_index('ix_orders_id', 'orders', ['id'], unique=False)
    # ### end Alembic commands ###
