from flask import Flask, request
from flask_restful import Api, Resource
from models import db, TaskModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


class TasksView(Resource):
    def get(self):
        tasks = TaskModel.query.all()
        return {'tasks': list(x.json() for x in tasks)}

    def post(self):
        data = request.get_json()

        new_task = TaskModel(data['status'])
        db.session.add(new_task)
        db.session.commit()
        return new_task.json(), 201


class TaskView(Resource):
    def get(self, pk):
        task = TaskModel.query.filter_by(pk=pk).first()
        if task:
            return task.json()
        return {'message': 'task not found'}, 404


api.add_resource(TasksView, '/tasks')
api.add_resource(TaskView, '/task/<pk>:int')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
