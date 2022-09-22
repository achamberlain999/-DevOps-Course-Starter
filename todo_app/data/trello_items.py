from todo_app.models.item import Item


class ItemProvider:
    def __init__(self, client):
        self._client = client
    
    def get_items(self):
        trello_items = self._client.get_trello_lists_with_cards()
        items = []
        
        for list in trello_items:
            for card in list['cards']:
                items.append(Item.from_trello_card(card, list))

        return items

    def add_item(self, title, description):
        self._client.add_item_to_list(title, description)

    def complete_item(self, id):
        self._client.complete_card(id)

    def uncomplete_item(self, id):
        self._client.uncomplete_card(id)

    def delete_item(self, id):
        self._client.delete_card(id)