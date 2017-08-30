'''
Shopping list class implementation
'''
class Shoppinglist(object):
    '''
    Class to implement shoppinglist object
    '''
    def __init__(self):
        self.shopping_list = []

    def view(self):
        '''
        View method of the shooping list to enable user to view items
        '''
        return self.shopping_list

    def add_item(self, item):
        '''
        Method to allow adding of items to list
        '''
        if item not in self.shopping_list:
            self.shopping_list.append(item)
        else:
            raise KeyError("The Item alredy exists")

    def delete_item(self, item):
        '''
        Method to allow deletion of items from list
        '''
        self.shopping_list.remove(item)

    def update(self, item, item2):
        '''
        Method to allow updating of list items
        '''
        for key, value in enumerate(self.shopping_list):
            if value == item:
                self.shopping_list[key] = item2
                