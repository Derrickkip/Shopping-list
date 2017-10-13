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

    def getid(self):
        return self.uid

    def __repr__(self):
        return ("%d email is %s username is %s")%(self.uid,self.email,self.username) 

class ShoppingList(object):
    """
    Shopping list object class declaration
    """
    def __init__(self, listid, name, description, itemnumber, datecreated, items):
        #unique ID for every shopping list
        self.listid = listid
        self.name = name
        self.description = description
        self.itemnumber = itemnumber
        self.datecreated = datecreated
        self.items = items

class Item(object):
    """
    Shopping list Items Object class declaration
    """
    def __init__(self, itemid, name, price):
        self.itemid = itemid
        self.name = name
        self.price = price
