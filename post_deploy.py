import os

# This is so, we can set proper type schema for the SQLAlchemy DB URI parser
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    os.environ["DATABASE_URL"] = database_url.replace("postgres://", "postgresql://", 1)
