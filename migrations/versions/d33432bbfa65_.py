"""empty message

Revision ID: d33432bbfa65
Revises: 785a57efffd0
Create Date: 2024-10-21 22:09:32.667547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd33432bbfa65'
down_revision: Union[str, None] = '785a57efffd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
