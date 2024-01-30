# Import packages / modules
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
import math
from forms import TaskForm

# Init flask
application = Flask(__name__)
app = application

# Set secret key for CSRF protection
app.config['SECRET_KEY'] = 'sdfsdfsdfsdf345dsfgsdf'  # Replace 'your_secret_key' with a secure key
# Set MongoDB URI and DB from config
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Init MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DB']]

# Routes
allTasks = []

# Generate a random integer based on the current time in UTC format
def IDgenerator():
    return math.floor((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())

# Home page with form
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()

    if form.validate_on_submit():
        new_task = {
            'task': form.task.data,
            'status': 'uncomplete',
            'creation_date': datetime.utcnow()
        }
        db.tasks.insert_one(new_task)
        return redirect(url_for('index'))

    all_tasks = db.tasks.find()
    return render_template('index.html', t=all_tasks, form=form)

# Create a new task
@app.route('/task', methods=['POST'])
def tasks():
    new_task = {
        'task': request.form['task'],
        'status': 'uncomplete',
        'creation_date': datetime.utcnow()
    }
    db.tasks.insert_one(new_task)
    return redirect(url_for('index'))

# Read a specific task
@app.route('/task/<id>', methods=['GET'])
def getTask(id):
    return id

# Update a task
@app.route('/updatetask/<taskID>', methods=['GET'])
def updateTask(taskID):
    the_task = db.tasks.find_one({'_id': taskID})
    return render_template('edit.html', task=the_task)

@app.route('/do_updatetask', methods=['POST'])
def do_updatetask():
    task_id = request.form['taskID']
    update_task = {
        'task': request.form['task'],
    }
    db.tasks.update_one({'_id': task_id}, {'$set': update_task})
    return redirect(url_for('index'))

# Delete a task
@app.route('/deletetask/<taskID>', methods=['GET'])
def deleteTask(taskID):
    db.tasks.delete_one({'_id': taskID})
    return redirect(url_for('index'))

# Complete a task
@app.route('/complete/<taskID>')
def complete(taskID):
    db.tasks.update_one({'_id': taskID}, {'$set': {'status': 'complete'}})
    return redirect(url_for('index'))

# Uncomplete a task
@app.route('/uncomplete/<taskID>')
def uncomplete(taskID):
    db.tasks.update_one({'_id': taskID}, {'$set': {'status': 'uncomplete'}})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
