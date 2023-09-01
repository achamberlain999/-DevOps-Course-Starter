class HomepageViewModel:
    def __init__(self, items, environment):
        self._items = items
        self.environment = environment

    @property
    def items(self):
        return self._items
    
    @property
    def completed_items(self):
        return [item for item in self._items if item.complete]
    
    @property
    def uncompleted_items(self):
        return [item for item in self._items if not item.complete]
