import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db
from src.models.BlogpostModel import *
from src.models.UserModels import *

env_name = os.getenv('FLASK_ENV')
app = create_app("development")

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()