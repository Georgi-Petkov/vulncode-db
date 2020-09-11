"""pii flags

Revision ID: 4d799bc13b95
Revises: 1af56ef5ac3c
Create Date: 2020-09-11 14:54:57.844887

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4d799bc13b95'
down_revision = '1af56ef5ac3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'user',
        sa.Column('hide_name', sa.Boolean(), nullable=False, default=True))
    op.add_column(
        'user',
        sa.Column('hide_picture', sa.Boolean(), nullable=False, default=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hide_picture')
    op.drop_column('user', 'hide_name')
    # ### end Alembic commands ###
