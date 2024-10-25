"""empty message

Revision ID: 432f997db3a6
Revises: e7359c131017
Create Date: 2024-10-21 22:16:34.398844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '432f997db3a6'
down_revision: Union[str, None] = 'e7359c131017'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
