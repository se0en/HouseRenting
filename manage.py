# -*- encoding=UTF-8 -*-

from HouseApp import app, db
from flask_script import Manager
#from datetime import DateTime

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    #write data
    db.session.commit()


if __name__ == '__main__':
    manager.run()