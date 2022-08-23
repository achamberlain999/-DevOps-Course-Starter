from todo_app.network.trello_client import get_trello_lists_with_cards, add_item_to_list, delete_card, complete_card, uncomplete_card


def get_items():
    trello_items = get_trello_lists_with_cards()
    items = []
    
    for list in trello_items:
        list_name = list['name']
        for card in list['cards']:
            print(card)
            items.append({
                'id': card['id'],
                'title': card['name'],
                'description': card['desc'],
                'complete': list_name == "Done"
            })

    return items

def add_item(title, description):
    item = { 'title': title, 'description': description, 'status': 'Not Started', 'complete': False }

    add_item_to_list(item)

    return item

def complete_item(id):
    complete_card(id)

def uncomplete_item(id):
    uncomplete_card(id)

def delete_item(id):
    delete_card(id)