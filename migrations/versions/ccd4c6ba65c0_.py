"""empty message

Revision ID: ccd4c6ba65c0
Revises: 73afc0ffecbb
Create Date: 2024-10-21 22:18:23.753168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ccd4c6ba65c0'
down_revision: Union[str, None] = '73afc0ffecbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
