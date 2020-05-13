"""Create users table

Revision ID: 2e5db0f99ad5
Revises: 
Create Date: 2020-05-13 06:53:44.042282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e5db0f99ad5'
down_revision = None
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
