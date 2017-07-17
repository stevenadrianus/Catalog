from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    email = Column(String(100),nullable=False)
    picture = Column(String(250))


class Catalog(Base):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    category = Column(String(25), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'           : self.name,
           'description'    : self.description,
           'id'             : self.id,
           'category'       : self.category,
       }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
