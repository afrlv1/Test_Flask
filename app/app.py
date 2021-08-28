#!flask/bin/python
from datetime import datetime

from flask import Flask, jsonify, abort, request, make_response
from whoosh.support import unicode

app = Flask(__name__)

url = ''

tasks = [
    {
        'id': 1,
        'status': 'In Queue',
        'create_time': '',
        'start_time': '',
        'time_to_execute': '10'
    },
    {
        'id': 2,
        'status': 'Run',
        'create_time': '',
        'start_time': '',
        'time_to_execute': '10'
    },
    {
        'id': 3,
        'status': 'Completed',
        'create_time': '',
        'start_time': '',
        'time_to_execute': '10'
    }
]


@app.route(url+'/', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route(url+'/<int:task_id>', methods=['GET'])
def get_task(task_id):
    _ = {}
    for task in tasks:
        if task['id'] == task_id:
            _ = task

    if len(_) == 0:
        abort(404)
    return jsonify(_)


@app.route(url+'/', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1,
        'status': 'In Queue',
        'create_time': datetime.now(),
        'start_time': '',
        'time_to_execute': '',
    }
    tasks.append(task)
    return jsonify({'id': task['id']}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
