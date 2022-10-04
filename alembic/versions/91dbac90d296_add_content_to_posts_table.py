"""add content to posts table

Revision ID: 91dbac90d296
Revises: 8bc0c1efa79a
Create Date: 2022-09-30 14:31:27.849899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "91dbac90d296"
down_revision = "8bc0c1efa79a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
