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
        for shop_list in self.shopping_lists:
            if shop_list.listid > shopping_list.listid:
                shop_list.listid -= 1

    def __repr__(self):
        return ("<Email: %s> <Username: %s>")%(self.email, self.username)

class ShoppingList(object):
    """
    Shopping list object class declaration
    """
    def __init__(self, listid, name, datecreated):
        #unique ID for every shopping list
        self.listid = listid
        self.name = name
        self.datecreated = datecreated
        self.items = []

    def update_list(self, update_name):
        """
        Update the shopping list
        """
        self.name = update_name

    def add_item(self, item):
        """
        Add items to shopping list
        """
        self.items.append(item)

    def count_items(self):
        """
        Method to count number of items
        """
        return len(self.items)

    def delete_item(self, item):
        """
        remove items from list
        """
        self.items.remove(item)
        for lstitem in self.items:
            if lstitem.itemid > item.itemid:
                lstitem.itemid -= 1

class Item(object):
    """
    Shopping list Items Object class declaration
    """
    def __init__(self, itemid, name):
        self.itemid = itemid
        self.name = name

    def update_item(self, update_name):
        """
        Update item
        """
        self.name = update_name
