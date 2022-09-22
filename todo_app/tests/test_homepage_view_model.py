from todo_app.view_models.homepage_view_model import HomepageViewModel
from todo_app.models.item import Item

class TestHomepageViewModel:
    def test_one(self):
        item = Item('ID', 'item_name', 'item_description', complete=False)

        model = HomepageViewModel([item])

        assert model.completed_items[0] == item