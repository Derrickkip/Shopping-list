"""
Shopping list app class definitions
"""
class User(object):
    """
    User object class declaration
    """
    def __init__(self, uid, Email, Username, Password):
        #user id
        self.uid = uid
        self.email = Email
        self.username = Username
        self.password = Password
        self.shopping_lists = []

    def add_list(self, shopping_list):
        """
        Add user lists
        """
        self.shopping_lists.append(shopping_list)

    def delete_list(self, shopping_list):
        """
        Delete user list
        """
        self.shopping_lists.remove(shopping_list)

    def __repr__(self):
        return ("<Email: %s> <Username: %s>")%(self.email, self.username)

class ShoppingList(object):
    """
    Shopping list object class declaration
    """
    def __init__(self, listid, name):
        #unique ID for every shopping list
        self.listid = listid
        self.name = name
        self.items = []

    def update_list(self, name2):
        """
        Update the shopping list
        """
        self.name = name2

    def add_item(self, item):
        """
        Add items to shopping list
        """
        self.items.append(item)

    def delete_item(self, item):
        """
        remove items from list
        """
        self.items.remove(item)

class Item(object):
    """
    Shopping list Items Object class declaration
    """
    def __init__(self, itemid, name):
        self.itemid = itemid
        self.name = name

    def update_item(self, name2):
        """
        Update item
        """
        self.name = name2
