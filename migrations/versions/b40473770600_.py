import sqlmodel
"""empty message

Revision ID: b40473770600
Revises: 1c54b55014bb
Create Date: 2024-10-21 22:01:30.746424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b40473770600'
down_revision: Union[str, None] = '1c54b55014bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
