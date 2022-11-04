import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request, redirect
from todo_app.view_models.homepage_view_model import HomepageViewModel
from todo_app.network.trello_client import TrelloClient
from todo_app.data.trello_items import ItemProvider

from todo_app.flask_config import Config

def create_item_provider():
    trello_client = TrelloClient(
        os.getenv('TRELLO_BOARD_ID'),
        os.getenv('TRELLO_API_BASE_URL'),
        os.getenv('TRELLO_API_KEY'),
        os.getenv('TRELLO_API_TOKEN')
    )

    return ItemProvider(trello_client)

def create_app(env_path='.env'):
    load_dotenv(find_dotenv(env_path))

    app = Flask(__name__)
    app.config.from_object(Config())

    item_provider = create_item_provider()

    @app.route('/')
    def index():
        items = item_provider.get_items()
        
        model = HomepageViewModel(items)
        return render_template('index.html', model=model)

    @app.route('/task', methods=['POST'])
    def add_new_task():
        title = request.form.get('new_task_title')
        description = request.form.get('new_task_description')
        
        if title:
            item_provider.add_item(title, description)

        return redirect('/')

    @app.route('/task/complete/<id>', methods=['POST'])
    def complete(id):
        item_provider.complete_item(id)

        return redirect('/')

    @app.route('/task/uncomplete/<id>', methods=['POST'])
    def uncomplete(id):
        item_provider.uncomplete_item(id)

        return redirect('/')

    @app.route('/task/delete/<id>', methods=['POST'])
    def delete(id):
        item_provider.delete_item(id)

        return redirect('/')
    
    return app

if __name__ == "__main__":
    create_app()