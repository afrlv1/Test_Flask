from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))
    create_time = db.Column(db.DateTime())
    start_time = db.Column(db.DateTime())
    time_to_execute = db.Column(db.String(80))

    def __init__(self, status):
        self.status = status
        self.create_time = datetime.now()
        self.start_time = datetime.now()
        self.time_to_execute = datetime.now()

    def json(self):
        return {
            "status": self.status,
            'create_time': str(self.create_time),
            'start_time': str(self.start_time),
            'time_to_execute': self.time_to_execute
        }