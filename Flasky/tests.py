'''
Tests for shoppinglist
'''

import unittest
from shoppinglist import Shoppinglist
from user import User
class test_user_registration(unittest.TestCase):
    '''
    User can register
    '''

class UserclassTests(unittest.TestCase):
    '''
    Test user can register and login into site
    '''
    def setUp(self):
        self.User = User()
        self.users_details = [{"derrick":"letmein"}, {"Michael":1234}]

    def test_login(self):
        auth = self.login(derrick, letmin)
        self.assertEqual(auth, 'Login successful')
        leave = self.logout()
        self.assertEqual(leave, 'You were logged out')

    def test_unknown_user(self):
        auth = self.login(michael, letmein)
        self.assertEqual(auth, "The username or password is wrong")
        wrong_password = self.login("derrick", "python")
        self.assertEqual(wrong_password, 'The username or password is wrong')



class ShoppinglistTest(unittest.TestCase):
    '''
    shoppinglist tests
    '''
    def setUp(self):
        self.shopping_list = Shoppinglist()

    def tearDown(self):
        self.shopping_list = None

    def test_can_view_list(self):
        '''
        Test for ability to view list
        '''
        self.assertEqual(self.shopping_list.view(), [])

    def test_add_item(self):
        '''
        Test that items can be added to shopping list
        '''
        self.shopping_list.add_item("book")
        self.assertEqual(self.shopping_list.view(), ["book"])

    def test_can_delete_item(self):
        '''
        Test that items can be deleted from shopping list
        '''
        self.shopping_list.add_item("books")
        self.shopping_list.add_item("pens")
        self.shopping_list.delete_item("books")
        self.assertEqual(self.shopping_list.view(), ["pens"])

    def test_can_update_item(self):
        '''
        Test that list items can be updated
        '''
        self.shopping_list.add_item("books")
        self.shopping_list.update("books", "Programming books")
        self.assertEqual(self.shopping_list.view(), ["Programming books"])

    def test_cannot_duplicate_items(self):
        '''
        Test that every list item is unique
        '''
        self.shopping_list.add_item("books")
        with self.assertRaises(KeyError):
            self.shopping_list.add_item("books")

if __name__ == '__main__':
    unittest.main()
