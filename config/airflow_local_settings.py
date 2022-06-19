import os

# This is to fix SQLAlchemy issue: https://github.com/sqlalchemy/sqlalchemy/issues/6083
SQL_ALCHEMY_CONN = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1)
