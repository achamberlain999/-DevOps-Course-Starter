from todo_app.models.item import Item


class ItemProvider:
    def __init__(self, client):
        self._client = client
    
    def get_items(self):
        mongodb_items = self._client.get_all_tasks()
        items = []
        
        for card in mongodb_items:
            items.append(Item.from_mongodb_entry(card))

        return items

    def add_item(self, title, description):
        self._client.add_item_to_list(title, description)

    def complete_item(self, id):
        self._client.complete_card(id)

    def uncomplete_item(self, id):
        self._client.uncomplete_card(id)

    def delete_item(self, id):
        self._client.delete_card(id)