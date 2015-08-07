import sqlalchemy as sa


engine = None


def get_engine():
    global engine
    if not engine:
        engine = sa.create_engine('sqlite:////tmp/testdb.sqlite',
                                  convert_unicode=True)
    return engine


def get_session():
    Session = sa.orm.sessionmaker(autocommit=False, autoflush=False,
                                  bind=get_engine())
    return sa.orm.scoped_session(Session)


Base = sa.ext.declarative.declarative_base()
Base.metadata.bind = get_engine()

class Session(Base):
    __tablename__ = 'session'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode)

Base.metadata.create_all()
