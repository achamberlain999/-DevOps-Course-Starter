class HomepageViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def completed_items(self):
        return self._items
    
    @property
    def uncompleted_items(self):
        return self._items
