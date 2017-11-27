from app.application import create_app
from app.extensions import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app('config.DevelopmentConfig')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    print('Starting the server')
    app.run(host=app.config['HOST'], port=app.config['PORT'])


if __name__ == "__main__":
    manager.run()
