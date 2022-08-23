from todo_app.network.trello_client import get_trello_lists_with_cards, add_item_to_list


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


def save_item(item):
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item

def delete_item(id):
    existing_items = get_items()
    updated_items = [existing_item for existing_item in existing_items if existing_item['id'] != id]

    session['items'] = updated_items