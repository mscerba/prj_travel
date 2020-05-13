"""Create users table

Revision ID: e86b8bd14453
Revises: 2e5db0f99ad5
Create Date: 2020-05-13 07:10:11.579797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e86b8bd14453'
down_revision = '2e5db0f99ad5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String)
    )


def downgrade():
    op.drop_table("user")
