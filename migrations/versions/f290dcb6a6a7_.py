"""empty message

Revision ID: f290dcb6a6a7
Revises: d548b8023b7d
Create Date: 2024-10-21 22:20:06.762422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'f290dcb6a6a7'
down_revision: Union[str, None] = 'd548b8023b7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
