"""empty message

Revision ID: 785a57efffd0
Revises: d93ee949da08
Create Date: 2024-10-21 22:09:18.690437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '785a57efffd0'
down_revision: Union[str, None] = 'd93ee949da08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
