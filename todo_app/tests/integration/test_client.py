import os
import pytest
import requests
import pymongo
from todo_app import app
import mongomock

@pytest.fixture
def client():
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app('test')
        with test_app.test_client() as client:
            yield client

@pytest.fixture
def mock_db():
    yield pymongo.MongoClient("mongodb://fakemongo.com")['test-tasko-database']

class TestClient:
    def test_index_page__with_no_cards(self, client):
        html = client.get('/').data.decode()

        assert "Time to start adding some tasks!" in html

    def test_index_page__with_todo_card_and_none_completed(self, client, mock_db):
        tasks = mock_db.tasks
        tasks.insert_one({
            'name': 'Todo card',
            'desc': 'Description',
            'list': 'To do'
        })
        html = client.get('/').data.decode()

        assert "Todo card" in html
        assert "Looks like you've got some work to do. Better knuckle down" in html

    def test_index_page__with_completed_card_and_none_to_do(self, client, mock_db):
        tasks = mock_db.tasks
        tasks.insert_one({
            'name': 'Completed card',
            'desc': 'Description',
            'list': 'Done'
        })
        html = client.get('/').data.decode()
        
        assert "Completed card" in html
        assert "Hurrah! Looks like it's pub time" in html

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_lists_stub(url, params=None):
    test_board_id = os.getenv('TRELLO_BOARD_ID')
    fake_response_data = None

    if url.startswith(f'https://api.trello.com/1/boards/{test_board_id}/lists'):
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card', 'desc': 'Description'}]
        }]
    
    return StubResponse(fake_response_data)