"""empty message

Revision ID: b38062c82ec8
Revises: 1537e4836b79
Create Date: 2020-01-22 19:18:21.441017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38062c82ec8'
down_revision = '1537e4836b79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('street', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='address_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='address_pkey')
    )
    op.drop_table('user_address')
    # ### end Alembic commands ###
