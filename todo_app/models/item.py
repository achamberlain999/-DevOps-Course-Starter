class Item:
    def __init__(self, id, name, description, complete = False):
        self.id = id
        self.name = name
        self.description = description
        self.complete = complete
    
    @classmethod
    def from_mongodb_entry(cls, card):
        return cls(card['_id'], card['name'], card['desc'], card['list'] == 'Done')