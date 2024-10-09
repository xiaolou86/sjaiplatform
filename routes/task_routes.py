from flask import Blueprint, jsonify, request
from models import db, Task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "name": task.name, "description": task.description} for task in tasks]
    return jsonify(task_list)

@task_bp.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(name=data['name'], description=data['description'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully!"}), 201

@task_bp.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify({"id": task.id, "name": task.name, "description": task.description})

@task_bp.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.name = data.get('name', task.name)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify({"message": "Task updated successfully!"})

@task_bp.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully!"})

