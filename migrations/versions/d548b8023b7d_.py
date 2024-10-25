"""empty message

Revision ID: d548b8023b7d
Revises: ccd4c6ba65c0
Create Date: 2024-10-21 22:19:15.846197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd548b8023b7d'
down_revision: Union[str, None] = 'ccd4c6ba65c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
