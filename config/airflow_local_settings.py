import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

print('!!!!Changing SQL_ALCHEMY_CONN!!!')
# This is to fix SQLAlchemy issue: https://github.com/sqlalchemy/sqlalchemy/issues/6083
globals()['SQL_ALCHEMY_CONN'] = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1)
