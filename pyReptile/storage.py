from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define data storage classes
class DataStorage(object):
    def __init__(self, DATABASE_CONNECTION, **kwargs):
        self.field()
        if kwargs.get('tablename', ''):
            tablename = kwargs['tablename']
        else:
            tablename = self.__class__.__name__
        self.table = self.table(tablename)
        self.DBSession = self.connect(DATABASE_CONNECTION)

    # Define table metadata
    def field(self):
        # define the fields for your item here like:
        # self.name = Column(String(50))
        pass

    # Connect to the database
    def connect(self, DATABASE_CONNECTION):
        engine = create_engine(DATABASE_CONNECTION)
        DBSession = sessionmaker(bind=engine)()
        Base.metadata.create_all(engine)
        return DBSession

    # Define declarative mapping
    def table(self, tablename):
        class TempTable(Base):
            __tablename__ = tablename
            id = Column(Integer, primary_key=True)

        for k, v in self.__dict__.items():
            if isinstance(v, Column):
                setattr(TempTable, k, v)
        return TempTable

    # Insert data
    def insert(self, value):
        self.DBSession.execute(self.table.__table__.insert(), value)
        self.DBSession.commit()

    # Update data
    def update(self, value, condition=None):
        if condition:
            c = self.table.__dict__[list(condition.keys())[0]].in_(list(condition.values()))
            self.DBSession.execute(self.table.__table__.update().where(c).values(), value)
        else:
            self.DBSession.execute(self.table.__table__.update().values(), value)
        self.DBSession.commit()

    # Download file
    def getfile(self, content, filepath):
        with open(filepath, 'wb') as code:
            code.write(content)
