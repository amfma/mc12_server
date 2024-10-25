"""empty message

Revision ID: ee25c1e4cd8f
Revises: e1efc03a5bc5
Create Date: 2024-10-21 22:23:33.553436

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ee25c1e4cd8f'
down_revision: Union[str, None] = 'e1efc03a5bc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
