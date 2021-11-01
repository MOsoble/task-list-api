"""empty message

Revision ID: dd8552ccee66
Revises: a9403fce2957
Create Date: 2021-11-01 22:14:17.071215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd8552ccee66'
down_revision = 'a9403fce2957'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('completed_at', sa.DateTime(), nullable=True))
    op.add_column('goal', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'description')
    op.drop_column('goal', 'completed_at')
    # ### end Alembic commands ###