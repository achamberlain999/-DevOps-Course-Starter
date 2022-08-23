from todo_app.network.trello_client import get_trello_lists_with_cards


def get_items():
    trello_items = get_trello_lists_with_cards()
    items = []
    
    for list in trello_items:
        list_name = list['name']
        for card in list['cards']:
            print(card)
            items.append({
                'title': card['name'],
                'description': card['desc'],
                'complete': list_name == "Done"
            })

    return items

def add_item(title, description):
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = max([item['id'] for item in items]) + 1 if items else 0

    item = { 'id': id, 'title': title, 'description': description, 'status': 'Not Started', 'complete': False }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item


def save_item(item):
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def delete_item(id):
    existing_items = get_items()
    updated_items = [existing_item for existing_item in existing_items if existing_item['id'] != id]

    session['items'] = updated_items