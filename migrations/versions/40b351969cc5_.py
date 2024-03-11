"""empty message

Revision ID: 40b351969cc5
Revises: efb09cb2c8ad
Create Date: 2024-03-05 13:57:12.075121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40b351969cc5'
down_revision = 'efb09cb2c8ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('x', sa.Text(), nullable=False))
    op.alter_column('blogposts', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('blogposts', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('blogposts', 'contents')
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.add_column('blogposts', sa.Column('contents', sa.TEXT(), autoincrement=False, nullable=True))
    op.alter_column('blogposts', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('blogposts', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.drop_column('blogposts', 'x')
    # ### end Alembic commands ###
