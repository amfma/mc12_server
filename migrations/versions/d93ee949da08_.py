"""empty message

Revision ID: d93ee949da08
Revises: eb861ed57684
Create Date: 2024-10-21 22:06:16.215625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd93ee949da08'
down_revision: Union[str, None] = 'eb861ed57684'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
