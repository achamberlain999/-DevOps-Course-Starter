from todo_app.view_models.homepage_view_model import HomepageViewModel
from todo_app.models.item import Item

class TestHomepageViewModel:
    def test_get_items(self):
        item = Item('ID', 'item_name', 'item_description', complete=False)

        model = HomepageViewModel([item])

        assert model.completed_items[0] == item
    
    def test_get_completed_items(self):
        uncompleted_item = Item('ID', 'item_name', 'item_description', complete=False)
        completed_item = Item('ID', 'item_name', 'item_description', complete=True)

        model = HomepageViewModel([uncompleted_item, completed_item])

        assert model.completed_items[0] == completed_item