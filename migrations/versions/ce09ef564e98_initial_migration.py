"""initial migration

Revision ID: be2c5a4ae2b4
Revises: 
Create Date: 2025-03-19 14:41:34.615823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be2c5a4ae2b4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """upgrade schema."""
    #all db changes
    pass


def downgrade() -> None:
    """Downgrade schema."""
    #former db changes
    pass
