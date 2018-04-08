"""
Shopping list flask implementation
"""
import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, session
from classes import User, ShoppingList, Item


SECRET_KEY = 'NaughtyNaughty'

FLASK_APP = Flask(__name__, template_folder='Designs', static_folder='Designs/static')
FLASK_APP.config.from_object(__name__)

USERLIST = {}
CURRENT_USER = {'logged_user': None}

def check_password(password1, password2):
    """
    helper function to compare passwords
    """
    return password1 == password2

def get_user():
    """
    helper function to get the current logged in user
    """
    user = CURRENT_USER.get('logged_user')
    return user

def get_shopping_list(user, listid):
    """
    Helper function to Get a specific shopping list from user
    """
    for shoplist in user.shopping_lists:
        if shoplist.listid == listid:
            current_list = shoplist
    return current_list

def get_shopping_list_item(user, listid, itemid):
    """
    Helper function to get an item from a list
    """
    current_list = get_shopping_list(user, listid)
    for item in current_list.items:
        if item.itemid == itemid:
            current_item = item
    return current_item

@FLASK_APP.route('/')
def home():
    """
    Home page view
    """
    return render_template('home.html')

@FLASK_APP.route('/registration', methods=["GET", "POST"])
def register():
    """
    Signup view
    """
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username']
        password1 = request.form['password']
        password2 = request.form['password2']
        if len(USERLIST) == 0:
            uid = 1
        else:
            uid = len(USERLIST) + 1
        if check_password(password1, password2) and email not in USERLIST:
            user = User(uid, email, username, password1)
            USERLIST[email] = user
            flash('Registration was successful you can now login')
            return redirect(url_for('login'))
        elif email in USERLIST:
            flash('The email is already in use on this site')
        else:
            flash('The two passwords do not match')

    return render_template('registration.html')

@FLASK_APP.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login view
    """
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if email in USERLIST:
            user = USERLIST[email]
            if check_password(user.password, password):
                flash('Login successful')
                session['logged_in'] = True
                CURRENT_USER['logged_user'] = user
                return redirect(url_for('shopping_list'))
            else:
                flash('The password does not match the one we have')
        else:
            flash('The email is not recognized')
    return render_template('login.html')

@FLASK_APP.route('/logout')
def logout():
    """
    logout view
    """
    session['logged_in'] = False
    CURRENT_USER['logged_user'] = None
    flash('You were logged out')
    return redirect(url_for('login'))

@FLASK_APP.route('/shoppinglists')
def shopping_list():
    """
    View Shopping lists
    """
    user = get_user()
    shopping_lists = user.shopping_lists
    return render_template('shoppinglists.html', shopping_lists=shopping_lists)

@FLASK_APP.route('/shoppinglists/add', methods=['GET', 'POST'])
def add_shopping_list():
    """
    Add shopping lists
    """
    user = get_user()
    if request.method == "POST":
        name = request.form["listname"]
        items = request.form["listitems"]
        items = items.split('\n')
        if len(user.shopping_lists) == 0:
            listid = 1
        else:
            listid = len(user.shopping_lists)+1
        today = datetime.date.today()
        shoplist = ShoppingList(listid, name, today)
        for item in items:
            if len(shoplist.items) == 0:
                itemid = 1
            else:
                itemid = shoplist.count_items() + 1
            if item:
                new_item = Item(itemid, item)
                shoplist.add_item(new_item)
        user.add_list(shoplist)
        return redirect(url_for('shopping_list'))
    return render_template('addshoppinglist.html')

@FLASK_APP.route('/shoppinglist/<int:listid>/update', methods=['GET', 'POST'])
def update_shoppinglist(listid):
    """
    Update the Shopping List
    """
    user = get_user()
    current_list = get_shopping_list(user, listid)
    items = [item.name for item in current_list.items]
    if request.method == 'POST':
        name = request.form.get('listname')
        items = request.form.get('listitems')
        items = items.split('\n')
        current_list.update_list(name)
        itemid = 1
        new_items = list()
        for item in items:
            new_item = Item(itemid, item)
            itemid += 1
            new_items.append(new_item)
        current_list.items = new_items
        return redirect(url_for('shopping_list'))

    return render_template('addshoppinglist.html', shoplist=current_list, items=items, edit=True)

@FLASK_APP.route('/shoppinglist/<int:listid>/delete')
def delete_list(listid):
    """
    Delete shoppinglist
    """
    user = get_user()
    current_list = get_shopping_list(user, listid)
    user.delete_list(current_list)
    return redirect(url_for('shopping_list'))

@FLASK_APP.route('/shoppinglist/<int:listid>/items')
def shoppinglist_items(listid):
    """
    View items of a shopping list
    """
    user = get_user()
    current_list = get_shopping_list(user, listid)
    return render_template('shoppingitems.html', shoplist=current_list, items=current_list.items)

@FLASK_APP.route('/shoppinglist/<int:listid>/items/delete/<int:itemid>')
def delete_item(listid, itemid):
    """
    view to delete item from shopping list
    """
    user = get_user()
    current_list = get_shopping_list(user, listid)
    selecteditem = get_shopping_list_item(user, listid, itemid)
    current_list.delete_item(selecteditem)
    return redirect(url_for('shoppinglist_items', listid=listid))

if __name__ == '__main__':
    FLASK_APP.run(debug=True)
