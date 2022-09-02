from flask import Flask, render_template, request, redirect
from todo_app.data.trello_items import complete_item, get_items, add_item, uncomplete_item, delete_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    completed_items = [item for item in items if item.complete]
    uncompleted_items = [item for item in items if not item.complete]

    return render_template('index.html', completed_items=completed_items, uncompleted_items=uncompleted_items)

@app.route('/task', methods=['POST'])
def add_new_task():
    title = request.form.get('new_task_title')
    description = request.form.get('new_task_description')
    
    if title:
        add_item(title, description)

    return redirect('/')

@app.route('/task/complete/<id>', methods=['POST'])
def complete(id):
    complete_item(id)

    return redirect('/')

@app.route('/task/uncomplete/<id>', methods=['POST'])
def uncomplete(id):
    uncomplete_item(id)

    return redirect('/')

@app.route('/task/delete/<id>', methods=['POST'])
def delete(id):
    delete_item(id)

    return redirect('/')