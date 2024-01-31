from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Task')

class UpdateTaskForm(FlaskForm):
    task = StringField('Task')
