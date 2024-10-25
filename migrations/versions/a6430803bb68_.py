"""empty message

Revision ID: a6430803bb68
Revises: d33432bbfa65
Create Date: 2024-10-21 22:11:47.464296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a6430803bb68'
down_revision: Union[str, None] = 'd33432bbfa65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
