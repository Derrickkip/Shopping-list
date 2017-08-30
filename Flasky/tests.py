import unittest
from shoppinglist import Shoppinglist

class ShoppinglistTest(unittest.TestCase):
    def setUp(self):
        self.shopping_list = Shoppinglist()

    def tearDown(self):
        self.shopping_list = None

    def test_can_view_list(self):
        self.assertEqual(self.shopping_list.view, [ ])

    def test_add_item(self):
        self.shopping_list.add_item("book")
        self.assertEqual(self.shopping_list, ["book"])

    def test_can_delete_item(self):
        self.shopping_list.add_item("books")
        self.shopping_list.add_item("pens")
        self.shopping_list.delete_item("books")
        self.assertEqual(self.shopping_list, ["pens"])

    def test_can_update_item(self):
        self.shopping_list.add_item("books")
        self.shopping_list.update("books", "Programming books")
        self.assertEqual(self.shopping_list, ["programming books"])

    def test_cannot_duplicate_items(self):
        self.shopping_list.add_item("books")
        with self.assertRaises(KeyError):
            self.shopping_list.add_item("books")

if __name__ == '__main__':
    unittest.main()
