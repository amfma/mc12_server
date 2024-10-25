"""empty message

Revision ID: e1efc03a5bc5
Revises: f290dcb6a6a7
Create Date: 2024-10-21 22:22:32.991810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'e1efc03a5bc5'
down_revision: Union[str, None] = 'f290dcb6a6a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
