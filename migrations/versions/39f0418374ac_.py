import sqlmodel
"""empty message

Revision ID: 39f0418374ac
Revises: 4c5dd712df48
Create Date: 2024-10-21 21:54:32.321387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39f0418374ac'
down_revision: Union[str, None] = '4c5dd712df48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
