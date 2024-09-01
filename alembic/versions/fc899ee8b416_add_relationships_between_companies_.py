"""add relationships between companies, users, and tasks

Revision ID: fc899ee8b416
Revises: 28ec438ff70b
Create Date: 2024-09-01 14:17:15.549037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = 'fc899ee8b416'
down_revision: Union[str, None] = '28ec438ff70b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add foreign key constraint to 'users' table linking to 'companies' table
    op.add_column('users', sa.Column('company_id', UUID(as_uuid=True), sa.ForeignKey('companies.id'), nullable=False))

    # Add foreign key constraint to 'tasks' table linking to 'users' table
    op.add_column('tasks', sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id'), nullable=False))

def downgrade() -> None:
    # Remove the foreign key and column from 'tasks' table
    op.drop_constraint('fk_tasks_user_id_users', 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'user_id')

    # Remove the foreign key and column from 'users' table
    op.drop_constraint('fk_users_company_id_companies', 'users', type_='foreignkey')
    op.drop_column('users', 'company_id')