"""empty message

Revision ID: 5505cc164b61
Revises: f1b17a2255c9
Create Date: 2020-12-20 19:51:22.449488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5505cc164b61'
down_revision = 'f1b17a2255c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
