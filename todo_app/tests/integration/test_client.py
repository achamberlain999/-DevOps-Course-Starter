import os
import pytest
import requests
from todo_app import app

@pytest.fixture
def client():
    test_app = app.create_app('test')

    with test_app.test_client() as client:
        yield client

class TestClient:
    def test_index_pages(self, monkeypatch, client):
        monkeypatch.setattr(requests, 'get', get_lists_stub)
        response = client.get('/')

        assert "Test card" in response.data.decode()

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