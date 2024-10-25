"""empty message

Revision ID: eb861ed57684
Revises: b40473770600
Create Date: 2024-10-21 22:05:23.774935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'eb861ed57684'
down_revision: Union[str, None] = 'b40473770600'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
