from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from resources.models import db
from app import app

migrate = Migrate(app, db, directory='db/migrations')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.config.from_object('config.BaseConfig')
    db.init_app(app)
    manager.run()
