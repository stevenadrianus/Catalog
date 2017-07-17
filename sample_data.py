
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Catalog, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo", email="Tinny@udacity.com",
             picture='''https://pbs.twimg.com/profile_images/2671170543/18debd69
             4829ed78203a5a36dd364160_400x400.png''')
session.add(User1)
session.commit()

User2 = User(name="Barista", email="Tim@udacity.com",
             picture='''https://pbs.twimg.com/profile_images/2671170543/18debd69
             4829ed78203a5a36dd364160_400x400.png''')
session.add(User2)
session.commit()
# Adding items
item1 = Catalog(name='Ball', description='To main item to play soccer',
                category='Soccer', user=User1 )

session.add(item1)
session.commit()

item1 = Catalog(name='Basketball', description='To main item to play Basket',
                category='Basket', user=User2 )
session.add(item1)
session.commit()
