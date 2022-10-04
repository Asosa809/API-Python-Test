"""create posts table

Revision ID: 8bc0c1efa79a
Revises: 
Create Date: 2022-09-30 14:18:44.664356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8bc0c1efa79a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
