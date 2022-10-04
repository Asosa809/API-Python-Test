"""add fk to posts table

Revision ID: 41e18c15fe0c
Revises: b1408a3a14f6
Create Date: 2022-09-30 14:42:35.734892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "41e18c15fe0c"
down_revision = "b1408a3a14f6"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint(
        "posts_users_fk",
        table_name="posts",
    )
    op.drop_column("posts", "owner_id")
    pass
