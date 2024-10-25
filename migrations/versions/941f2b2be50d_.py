import sqlmodel
"""empty message

Revision ID: 941f2b2be50d
Revises: 39f0418374ac
Create Date: 2024-10-21 21:55:17.681911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '941f2b2be50d'
down_revision: Union[str, None] = '39f0418374ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
