class HomepageViewModel:
    def __init__(self, completed_items, uncompleted_items):
        self._completed_items = completed_items
        self._uncompleted_items = uncompleted_items
    
    @property
    def completed_items(self):
        return self._completed_items
    
    @property
    def uncompleted_items(self):
        return self._uncompleted_items
