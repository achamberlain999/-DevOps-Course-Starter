import requests

class TrelloClient:
    def __init__(self, board_id, trello_api_base_url, trello_api_key, trello_api_token):
        self.BOARD_ID = board_id
        self.TRELLO_API_BASE_URL = trello_api_base_url
        self.TRELLO_API_KEY = trello_api_key
        self.TRELLO_API_TOKEN = trello_api_token
        self.LIST_IDS = {
            'To do': None,
            'Done': None
        }

    def url_builder(self, route):
        return f"{self.TRELLO_API_BASE_URL}{route}?key={self.TRELLO_API_KEY}&token={self.TRELLO_API_TOKEN}"

    def get_list_ids_if_null(self):
        if (self.LIST_IDS['To do'] and self.LIST_IDS['Done']):
            return

        url = self.url_builder(f"/boards/{self.BOARD_ID}/lists")
        r = requests.get(url)
        
        self.LIST_IDS['To do'] = next(l['id'] for l in r.json() if l['name'] == 'To do')
        self.LIST_IDS['Done'] = next(l['id'] for l in r.json() if l['name'] == 'Done')

    def get_trello_lists_with_cards(self):
        payload = {
            'cards': 'open'
        }
        url = self.url_builder(f"/boards/{self.BOARD_ID}/lists")
        r = requests.get(url, params=payload)
        return r.json()

    def add_item_to_list(self, title, description):
        url = self.url_builder(f"/cards")
        self.get_list_ids_if_null()
        payload = {
            'name': title,
            'desc': description,
            'idList': self.LIST_IDS['To do']
        }
        r = requests.post(url, params=payload)
        return r.json()

    def complete_card(self, id):
        url = self.url_builder(f"/cards/{id}")
        self.get_list_ids_if_null()
        payload = {
            'idList': self.LIST_IDS['Done']
        }
        r = requests.put(url, params=payload)
        return r.json()

    def uncomplete_card(self, id):
        url = self.url_builder(f"/cards/{id}")
        self.get_list_ids_if_null()
        payload = {
            'idList': self.LIST_IDS['To do']
        }
        r = requests.put(url, params=payload)
        return r.json()

    def delete_card(self, id):
        url = self.url_builder(f"/cards/{id}")
        r = requests.delete(url)
        return r.json()