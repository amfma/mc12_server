"""empty message

Revision ID: 73afc0ffecbb
Revises: 432f997db3a6
Create Date: 2024-10-21 22:17:41.807436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '73afc0ffecbb'
down_revision: Union[str, None] = '432f997db3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
