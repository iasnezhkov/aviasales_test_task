"""empty message

Revision ID: e5e9ae4dbbfc
Revises: 
Create Date: 2019-09-26 19:09:09.721436

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import models

# revision identifiers, used by Alembic.
revision = 'e5e9ae4dbbfc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('types', sa.ARRAY(sa.String(length=10)), nullable=True),
    sa.Column('origins', sa.ARRAY(sa.String(length=4)), nullable=True),
    sa.Column('destinations', sa.ARRAY(sa.String(length=4)), nullable=True),
    sa.Column('departure_dates', sa.ARRAY(sa.String(length=10)), nullable=True),
    sa.Column('return_dates', sa.ARRAY(sa.String(length=10)), nullable=True),
    sa.Column('adults', sa.Integer(), nullable=True),
    sa.Column('childs', sa.Integer(), nullable=True),
    sa.Column('infants', sa.Integer(), nullable=True),
    sa.Column('flight_classes', postgresql.ARRAY(sa.String(length=1)), nullable=True),
    sa.Column('airlines', postgresql.ARRAY(sa.String(length=2)), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('origin', sa.String(length=4), nullable=True),
    sa.Column('destination', sa.String(length=4), nullable=True),
    sa.Column('adults', sa.Integer(), nullable=True),
    sa.Column('childs', sa.Integer(), nullable=True),
    sa.Column('infants', sa.Integer(), nullable=True),
    sa.Column('total_duration', sa.Integer(), nullable=True),
    sa.Column('prices', models.product.CastingArray(postgresql.JSON(astext_type=sa.Text())), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('price_currency', sa.String(length=3), nullable=True),
    sa.Column('airlines', postgresql.ARRAY(sa.String(length=2)), nullable=True),
    sa.Column('departure_date', sa.Date(), nullable=True),
    sa.Column('return_date', sa.Date(), nullable=True),
    sa.Column('flight_classes', postgresql.ARRAY(sa.String(length=1)), nullable=True),
    sa.Column('search_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('carrier', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('flight_number', sa.Integer(), nullable=True),
    sa.Column('origin', sa.String(length=4), nullable=True),
    sa.Column('destination', sa.String(length=4), nullable=True),
    sa.Column('departure_date', sa.DateTime(), nullable=True),
    sa.Column('arrival_date', sa.DateTime(), nullable=True),
    sa.Column('flight_class', sa.String(length=1), nullable=True),
    sa.Column('stops', sa.Integer(), nullable=True),
    sa.Column('fare_basis', sa.String(length=255), nullable=True),
    sa.Column('warning_text', sa.String(length=255), nullable=True),
    sa.Column('ticket_type', sa.String(length=1), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flight')
    op.drop_table('product')
    op.drop_table('search')
    # ### end Alembic commands ###
