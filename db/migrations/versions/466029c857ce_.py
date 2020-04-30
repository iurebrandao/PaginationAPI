"""empty message

Revision ID: 466029c857ce
Revises: 
Create Date: 2020-04-30 01:23:22.162579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '466029c857ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('designation', sa.String(length=128), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('province', sa.String(length=255), nullable=True),
    sa.Column('region_1', sa.String(length=255), nullable=True),
    sa.Column('region_2', sa.String(length=255), nullable=True),
    sa.Column('taster_name', sa.String(length=255), nullable=True),
    sa.Column('taster_twitter_handle', sa.String(length=255), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('variety', sa.String(length=255), nullable=True),
    sa.Column('winery', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wine')
    # ### end Alembic commands ###
