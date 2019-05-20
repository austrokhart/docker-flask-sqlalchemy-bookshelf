
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import db_host, db_name, db_user, db_password


engine = create_engine("mysql://{}:{}@{}/{}".format(db_user, db_password, db_host, db_name), convert_unicode=True, echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


def database_init():
    Base.metadata.create_all(bind=engine)


def flask_connect(app):

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        session.remove()
