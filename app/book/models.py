
from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(80), nullable=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
