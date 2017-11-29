import os
import glob
import traceback
from os.path import dirname, basename, isfile, join

from app.database.models.positions import Position
from app.extensions import db


def seed_test_data():
    """
    This function runs/imports all scripts in the ./seeds directory. To add a new seed, simply create a new
    script that commits to the database and add it to the ./seeds folder.
    """
    seeds_dir = join(dirname(__file__), 'seeds')

    module_paths = []
    for root, dirs, files in os.walk(seeds_dir):
        files = glob.glob(root + '/[!_]*.py')
        for file in files:
            if isfile(file):
                parent_dir = file.split('\\')[-2]
                module_name = basename(file)[:-3]
                module_paths.append(
                    'app.database.seed.seeds.{}.{}'.format(parent_dir, module_name))

    for module_path in module_paths:
        try:
            print('-Running seed script: {}'.format(module_path))
            __import__(module_path)
        except Exception as e:
            print(e)
            traceback.print_exc()

    db.session.commit()


def seed_defaults():
    db.session.add_all([
        Position(id=1, name='Forward'),
        Position(id=2, name='Midfield'),
        Position(id=3, name='Defense'),
        Position(id=4, name='Goalkeeper')
    ])
    db.session.commit()
