import os
import requests

BOARD_ID = os.getenv('TRELLO_BOARD_ID')
TODO_LIST_ID = False

def get_todo_list_id():    
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url)
    
    TODO_LIST_ID = next(l['id'] for l in r.json() if l['name'] == 'Open')
    return TODO_LIST_ID

def get_todo_list_id_from_cache_or_fetch():
    if TODO_LIST_ID:
        return TODO_LIST_ID
    
    return get_todo_list_id()

def url_builder(route):
    return f"{os.getenv('TRELLO_API_BASE_URL')}{route}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"

def get_lists():
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url)
    return r.json()

def get_cards_in_list(list_id):
    url = url_builder(f"/lists/{list_id}/cards")
    r = requests.get(url)
    return r.json()

def get_trello_lists_with_cards():
    payload = {
        'cards': 'open'
    }
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url, params=payload)
    return r.json()

def add_item_to_list(item):
    url = url_builder(f"/cards")
    payload = {
        'name': item['title'],
        'desc': item['description'],
        'idList': get_todo_list_id()
    }
    r = requests.post(url, params=payload)
    return r.json()

# lists = get_lists()
# for l in lists:
#     print(l['name'])
#     cards = get_cards_in_list(l['id'])
#     for c in cards:
#         print('- ', c['name'])