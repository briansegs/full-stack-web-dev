"""empty message

Revision ID: bb12eb0167ab
Revises: 5505cc164b61
Create Date: 2020-12-21 12:15:14.544006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb12eb0167ab'
down_revision = '5505cc164b61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###
