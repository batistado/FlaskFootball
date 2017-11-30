import os

import app.database.seed.seed_helper as helper
from app.translation.deserializer import Deserializer
from app.extensions import db


real_madrid = {
    'name': 'Real Madrid CF',
    'players': helper.read_csv_file(os.path.join(os.path.dirname(__file__), 'players.csv')),
    'stadium': 'Santiago Bernabeu',
    'manager': 'Zinedine Zindane',
    'location': 'Madrid, Spain',
    'logo': 'real-madrid.jpg',
}

team = Deserializer().deserialize_team(real_madrid)
db.session.add(team)
