import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template, request, redirect
from todo_app.view_models.homepage_view_model import HomepageViewModel
from todo_app.network.mongodb_client import MongoDBClient
from todo_app.data.mongodb_items import ItemProvider

from todo_app.flask_config import Config

def create_item_provider(environment):
    mongodb_client = MongoDBClient(
        os.getenv('DATABASE_CONNECTION_STRING'),
        environment
    )

    return ItemProvider(mongodb_client)

def get_env_path(environment):
    if environment == 'test':
        return 'env/.env.test'
    else:
        # Currently development and production are using the same credentials
        # Which is obviously bad but we will change this later
        return '.env'

def create_app(environment='development'):
    print(f"Running the app...\nEnvironment: ${environment}")
    env_path = get_env_path(environment)
    load_dotenv(find_dotenv(env_path))

    app = Flask(__name__)
    app.config.from_object(Config())

    item_provider = create_item_provider(environment)

    @app.route('/')
    def index():
        items = item_provider.get_items()
        
        model = HomepageViewModel(items, environment)
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