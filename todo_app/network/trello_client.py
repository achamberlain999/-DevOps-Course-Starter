import os
import requests

BOARD_ID = os.getenv('TRELLO_BOARD_ID')

LIST_IDS = {
    'Open': False,
    'Done': False
}

def url_builder(route):
    return f"{os.getenv('TRELLO_API_BASE_URL')}{route}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"

def get_list_ids():    
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url)
    
    LIST_IDS['Open'] = next(l['id'] for l in r.json() if l['name'] == 'Open')
    LIST_IDS['Done'] = next(l['id'] for l in r.json() if l['name'] == 'Done')

get_list_ids()

def get_trello_lists_with_cards():
    payload = {
        'cards': 'open'
    }
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url, params=payload)
    return r.json()

def add_item_to_list(title, description):
    url = url_builder(f"/cards")
    payload = {
        'name': title,
        'desc': description,
        'idList': LIST_IDS['Open']
    }
    r = requests.post(url, params=payload)
    return r.json()

def complete_card(id):
    url = url_builder(f"/cards/{id}")
    payload = {
        'idList': LIST_IDS['Done']
    }
    r = requests.put(url, params=payload)
    return r.json()

def uncomplete_card(id):
    url = url_builder(f"/cards/{id}")
    payload = {
        'idList': LIST_IDS['Open']
    }
    r = requests.put(url, params=payload)
    return r.json()

def delete_card(id):
    url = url_builder(f"/cards/{id}")
    r = requests.delete(url)
    return r.json()