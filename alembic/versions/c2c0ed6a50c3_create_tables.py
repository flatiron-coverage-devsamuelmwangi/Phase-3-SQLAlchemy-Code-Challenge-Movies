"""Create tables

Revision ID: c2c0ed6a50c3
Revises: 
Create Date: 2023-06-14 12:03:06.860228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2c0ed6a50c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'actors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'movies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('box_office_earnings', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), nullable=True),
        sa.Column('actor_id', sa.Integer(), nullable=True),
        sa.Column('salary', sa.Integer(), nullable=True),
        sa.Column('character_name', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
        sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('roles')
    op.drop_table('movies')
    op.drop_table('actors')
