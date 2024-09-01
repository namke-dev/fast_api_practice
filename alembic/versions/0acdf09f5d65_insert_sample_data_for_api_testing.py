"""insert sample data for API testing

Revision ID: 0acdf09f5d65
Revises: fc899ee8b416
Create Date: 2024-09-01 14:20:15.561038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '0acdf09f5d65'
down_revision: Union[str, None] = 'fc899ee8b416'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Insert sample data into the companies table
    op.execute(
        f"""
        INSERT INTO companies (id, name, description, mode, rating) VALUES
        ('{uuid.uuid4()}', 'TechCorp', 'A leading tech company', 'remote', 5),
        ('{uuid.uuid4()}', 'HealthPlus', 'Healthcare services provider', 'onsite', 4);
        """
    )

    # Insert sample data into the users table
    company_id_techcorp = "SELECT id FROM companies WHERE name='TechCorp' LIMIT 1"
    company_id_healthplus = "SELECT id FROM companies WHERE name='HealthPlus' LIMIT 1"
    op.execute(
        f"""
        INSERT INTO users (id, company_id, username, email, first_name, last_name, password, is_active, is_admin) VALUES
        ('{uuid.uuid4()}', ({company_id_techcorp}), 'jdoe', 'jdoe@techcorp.com', 'John', 'Doe', 'password123', true, false),
        ('{uuid.uuid4()}', ({company_id_healthplus}), 'asmith', 'asmith@healthplus.com', 'Alice', 'Smith', 'password456', true, true);
        """
    )

    # Insert sample data into the tasks table
    user_id_jdoe = "SELECT id FROM users WHERE username='jdoe' LIMIT 1"
    user_id_asmith = "SELECT id FROM users WHERE username='asmith' LIMIT 1"
    op.execute(
        f"""
        INSERT INTO tasks (id, user_id, summary, description, status, priority) VALUES
        ('{uuid.uuid4()}', ({user_id_jdoe}), 'Fix Bug #123', 'Fix the issue with the login form', 'open', 1),
        ('{uuid.uuid4()}', ({user_id_asmith}), 'Develop Feature XYZ', 'Implement the new feature as discussed', 'in_progress', 2);
        """
    )


def downgrade() -> None:
    # Delete the sample data from the tasks table
    op.execute("DELETE FROM tasks WHERE summary IN ('Fix Bug #123', 'Develop Feature XYZ')")

    # Delete the sample data from the users table
    op.execute("DELETE FROM users WHERE username IN ('jdoe', 'asmith')")

    # Delete the sample data from the companies table
    op.execute("DELETE FROM companies WHERE name IN ('TechCorp', 'HealthPlus')")