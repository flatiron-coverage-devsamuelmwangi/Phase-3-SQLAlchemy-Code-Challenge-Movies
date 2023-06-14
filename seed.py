from lib.models import Actor, Movie, Role
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random


engine = create_engine('sqlite:///lib/db/movies.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of the classes and add data
actor1 = Actor(name='Actor 1')
actor2 = Actor(name='Actor 2')
movie1 = Movie(title='Movie 1', box_office_earnings=100000000)
movie2 = Movie(title='Movie 2', box_office_earnings=50000000)

role1 = Role(actor=actor1, movie=movie1, character_name='Character 1', salary=1000000)
role2 = Role(actor=actor2, movie=movie1, character_name='Character 2', salary=500000)
role3 = Role(actor=actor2, movie=movie2, character_name='Character 3', salary=800000)

session.add_all([actor1, actor2, movie1, movie2, role1, role2, role3])
session.commit()

# Test the object relationship methods
print(actor1.movies())  # List of movies for actor1
print(movie1.actors())  # List of actors
