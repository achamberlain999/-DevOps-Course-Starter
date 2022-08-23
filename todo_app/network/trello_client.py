import os
import requests

BOARD_ID = os.getenv('TRELLO_BOARD_ID')

def url_builder(route):
    return f"{os.getenv('TRELLO_API_BASE_URL')}{route}?key={os.getenv('TRELLO_API_KEY')}&token={os.getenv('TRELLO_API_TOKEN')}"

url = url_builder(f"/boards/{os.getenv('TRELLO_BOARD_ID')}/lists")
print(url)
r = requests.get(url)

print(r, r.status_code)
print(r.json())

for list in r.json():
    print(list['id'], list['name'])

def get_lists():
    url = url_builder(f"/boards/{BOARD_ID}/lists")
    r = requests.get(url)
    return r.json()

def get_cards_in_list(list_id):
    url = url_builder(f"/lists/{list_id}/cards")
    r = requests.get(url)
    return r.json()

lists = get_lists()
for l in lists:
    print(l['name'])
    cards = get_cards_in_list(l['id'])
    for c in cards:
        print('- ', c['name'])