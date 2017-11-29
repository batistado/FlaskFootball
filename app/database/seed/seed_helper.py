import csv
from app.extensions import db
from sqlalchemy import func
from app.database import Position


def read_csv_file(file):
    output = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if not line:
                continue
            line = trim(line)
            output.append(
                {
                    'name': line[0],
                    'rating': line[1],
                    'position': {
                        'id': get_position_id(line[2]),
                    },
                    'age': line[3],
                    'starter': 1 if line[4] == 'True' else 0,
                }
            )
    return output


def get_position_id(pos):
    position = db.session.query(Position).filter(func.lower(Position.name) == func.lower(pos)).first()
    if position is None:
        raise ValueError
    return position.id


def trim(line):
    trimmed_line = []
    for field in line:
        trimmed_line.append(field.strip())
    return trimmed_line

