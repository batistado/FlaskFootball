import os

import app.database.seed.seed_helper as helper
from app.translation.deserializer import Deserializer
from app.extensions import db

fc_barcelona = {
    'name': 'FC Barcelona',
    'players': helper.read_csv_file(os.path.join(os.path.dirname(__file__), 'players.csv')),
    'stadium': 'Camp Nou',
    'manager': 'Ernesto Valverde',
    'location': 'Catalonia, Spain',
    'logo': 'fc-barcelona.jpg',
}

team = Deserializer().deserialize_team(fc_barcelona)
db.session.add(team)
