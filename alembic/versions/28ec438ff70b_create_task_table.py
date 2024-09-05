"""create task table

Revision ID: 28ec438ff70b
Revises: 71293c04480e
Create Date: 2024-09-01 11:59:07.569918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import uuid
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '28ec438ff70b'
down_revision: Union[str, None] = '71293c04480e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('summary', sa.String(255), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('priority', sa.SmallInteger, nullable=False),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('tasks')

