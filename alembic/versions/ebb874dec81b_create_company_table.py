"""create company table

Revision ID: ebb874dec81b
Revises: 
Create Date: 2024-09-01 11:58:45.693649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = 'ebb874dec81b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'companies',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('mode', sa.String(50), nullable=False),
        sa.Column('rating', sa.SmallInteger, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('companies')

