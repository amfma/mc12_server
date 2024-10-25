"""empty message

Revision ID: e7359c131017
Revises: a6430803bb68
Create Date: 2024-10-21 22:15:58.593791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e7359c131017'
down_revision: Union[str, None] = 'a6430803bb68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
