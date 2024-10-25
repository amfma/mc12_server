import sqlmodel
"""empty message

Revision ID: 1c54b55014bb
Revises: 941f2b2be50d
Create Date: 2024-10-21 21:58:03.557295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c54b55014bb'
down_revision: Union[str, None] = '941f2b2be50d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
