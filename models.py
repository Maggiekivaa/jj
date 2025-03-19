from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()
class Books(Base):

    __tablename__ = "books"

    id = Column(Integer(), primary_key=True)

    name = Column(String())
    book_no = Column(Integer())
    pass

class author(Base):
     __tablename__ = "authors"

     id = Column(Integer(), primary_key=True)

     name = Column(String())

class user(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)

    name = Column(String())

          



library_engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(library_engine)