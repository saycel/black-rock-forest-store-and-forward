import os

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import config

if os.environ['FLASK_ENV'] == 'development':
    db_uri = config.DEV_DATABASE_URI
elif os.environ['FLASK_ENV'] == 'production':
    db_uri = config.PROD_DATABASE_URI
else:
    sys.exit(0)

engine = create_engine(db_uri,
                       convert_unicode=True,
                       echo=True
                      )

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(engine)
