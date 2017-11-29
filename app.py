from app.application import create_app
from app.extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import app.database.seed.seed as seed_helper

app = create_app('config.DevelopmentConfig')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    print('Starting the server')
    app.run(host=app.config['HOST'], port=app.config['PORT'])


@manager.command
def seed():
    print('Dropping all tables')
    db.drop_all()
    db.create_all()
    seed_helper.seed_defaults()
    seed_helper.seed_test_data()
    print('Seeding test data complete.')


if __name__ == "__main__":
    manager.run()
