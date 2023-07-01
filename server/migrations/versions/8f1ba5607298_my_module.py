"""My module

Revision ID: 8f1ba5607298
Revises: 5d7e7a63927c
Create Date: 2023-07-02 00:43:28.818425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1ba5607298'
down_revision = '5d7e7a63927c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('plant')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('image', sa.VARCHAR(length=255), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('plants')
    # ### end Alembic commands ###
