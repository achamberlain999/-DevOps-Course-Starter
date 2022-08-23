from todo_app.network.trello_client import get_trello_lists_with_cards, add_item_to_list, delete_card, complete_card, uncomplete_card
from todo_app.models.item import Item

def get_items():
    trello_items = get_trello_lists_with_cards()
    items = []
    
    for list in trello_items:
        for card in list['cards']:
            items.append(Item.from_trello_card(card, list))

    return items

def add_item(title, description):
    add_item_to_list(title, description)

def complete_item(id):
    complete_card(id)

def uncomplete_item(id):
    uncomplete_card(id)

def delete_item(id):
    delete_card(id)