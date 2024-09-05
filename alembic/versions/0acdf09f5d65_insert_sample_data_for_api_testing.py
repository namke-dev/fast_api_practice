"""insert sample data for API testing

Revision ID: 0acdf09f5d65
Revises: 28ec438ff70b
Create Date: 2024-09-01 14:20:15.561038

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text
import uuid
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '0acdf09f5d65'
down_revision: Union[str, None] = '28ec438ff70b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Insert sample data into the companies table
    op.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")

    op.execute(
        """
        INSERT INTO companies (id, name, description, mode, rating) VALUES
        (uuid_generate_v4(), 'TechCorp', 'A leading tech company', 'remote', 5),
        (uuid_generate_v4(), 'HealthPlus', 'Healthcare services provider', 'onsite', 4);
        """
    )

    # Fetch company IDs
    company_id_techcorp = op.get_bind().execute(
        text("SELECT id FROM companies WHERE name='TechCorp' LIMIT 1")
    ).scalar()

    company_id_healthplus = op.get_bind().execute(
        text("SELECT id FROM companies WHERE name='HealthPlus' LIMIT 1")
    ).scalar()

    # Insert sample data into the users table
    op.execute(
        f"""
        INSERT INTO users (id, company_id, username, email, first_name, last_name, password, is_active, is_admin) VALUES
        (uuid_generate_v4(), '{company_id_techcorp}', 'admin', 'admin@techcorp.com', 'John', 'Doe', '123456', true, false),
        (uuid_generate_v4(), '{company_id_healthplus}', 'user1', 'user1@healthplus.com', 'Alice', 'Smith', '123456', true, true);
        """
    )

    # Fetch user IDs
    user_id_admin = op.get_bind().execute(
        text("SELECT id FROM users WHERE username='admin' LIMIT 1")
    ).scalar()

    user_id_user1 = op.get_bind().execute(
        text("SELECT id FROM users WHERE username='user1' LIMIT 1")
    ).scalar()

    # Insert sample data into the tasks table
    op.execute(
        f"""
        INSERT INTO tasks (id, user_id, summary, description, status, priority) VALUES
        (uuid_generate_v4(), '{user_id_admin}', 'Fix Bug #123', 'Fix the issue with the login form', 'open', 1),
        (uuid_generate_v4(), '{user_id_user1}', 'Develop Feature XYZ', 'Implement the new feature as discussed', 'in_progress', 2);
        """
    )


def downgrade() -> None:
    # Delete the sample data from the tasks table
    op.execute("DELETE FROM tasks")

    # Delete the sample data from the users table
    op.execute("DELETE FROM users")

    # Delete the sample data from the companies table
    op.execute("DELETE FROM companies")