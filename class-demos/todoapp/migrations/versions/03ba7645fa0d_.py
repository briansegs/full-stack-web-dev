"""empty message

Revision ID: 03ba7645fa0d
Revises: 96318491ccb7
Create Date: 2020-12-17 14:23:09.169360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ba7645fa0d'
down_revision = '96318491ccb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')

    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###