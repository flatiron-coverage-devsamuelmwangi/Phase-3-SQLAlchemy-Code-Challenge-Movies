#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb;
from lib.models import Actor, Movie, Role

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///lib/db/movies.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
