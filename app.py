"""
Shopping list flask implementation
"""
from flask import Flask, render_template, request, flash, redirect, url_for, session
from classes import User, ShoppingList, Item

SECRET_KEY = 'NaughtyNaughty'

FLASK_APP = Flask(__name__, template_folder='Designs', static_folder='Designs/static')
FLASK_APP.config.from_object(__name__)

USERLIST = {}
CURRENT_USER = {}

def check_password(password1, password2):
    """
    helper function to compare passwords
    """
    same = False
    if password1 == password2:
        same = True
    return same

@FLASK_APP.route('/')
def home():
    """
    Home page view
    """
    return render_template('home.html')

@FLASK_APP.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration view
    """
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['passwd']
        if USERLIST == {}:
            uid = 1
        else:
            uid = len(USERLIST.items())+1
        if check_password(password, password2):
            user = User(uid, email, username, password)
            USERLIST[username] = user
            flash('Registration successful you can now login')
            return redirect(url_for('login'))
        else:
            flash("The passwords do not match")
    return render_template('registration.html')

@FLASK_APP.route('/login', methods=['GET', 'POST'])
def login():
    """
    User Login view
    """
    if request.method == 'POST':
        #get username and password from the request object
        username = request.form['username']
        password = request.form['password']
        if username in USERLIST:
            user = USERLIST[username]
            saved_password = user.password
            #check that password provided is same as the stored password
            if not check_password(saved_password, password):
                flash('Incorrect password')
            else:
                flash("Login successful")
                session['logged_in'] = True
                CURRENT_USER['logged_user'] = user
                return redirect(url_for('shopping_list'))
        else:
            flash('The username is not recognised')
    return render_template('login.html')

@FLASK_APP.route('/logout')
def logout():
    """
    View to log user out of the FLASK_APP
    """
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@FLASK_APP.route('/shopping-list')
def shopping_list():
    """
    view for showing shopping lists
    """
    user = CURRENT_USER['logged_user'] or None
    user_lists = user.shopping_lists
    return render_template('shoppinglist.html', user_lists=user_lists)

@FLASK_APP.route('/shopping-list/add', methods=['POST'])
def add_shopping_list():
    """
    add shopping list
    """
    #get current user object
    user = CURRENT_USER['logged_user']
    if user:
        #get users shopping lists
        user_lists = user.shopping_lists
        #
        if user_lists == []:
            uid = 1
        else:
            uid = len(user_lists)+1
        name = str(request.form['shoplist'])
        shoplist = ShoppingList(uid, name)
        user.add_list(shoplist)
        flash('List successfully added')
        return redirect(url_for('shopping_list'))

@FLASK_APP.route('/shopping-list/delete/<int:listid>')
def delete_shopping_list(listid):
    """
    Delete shopping list
    """
    #get current user object
    user = CURRENT_USER['logged_user']
    if user:
        #get users shopping list
        shopping_lists = user.shopping_lists
        for shoplist in shopping_lists:
            #get shopping list with the specified id
            if shoplist.listid == listid:
                #delete shopping list
                user.delete_list(shoplist)
                flash('Shopping list deleted')
                return redirect(url_for('shopping_list'))

@FLASK_APP.route('/shopping-list/update/<int:listid>', methods=['GET', 'POST'])
def update_shopping_list(listid):
    """
    Update shopping list
    """
    user = CURRENT_USER['logged_user']
    shopping_lists = user.shopping_lists
    if request.method == "POST":
        for shoplist in shopping_lists:
            if shoplist.listid == listid:
                shoplist.update_list(request.form['listname'])
                return redirect(url_for('shopping_list'))
    else:
        for shoplist in shopping_lists:
            if shoplist.listid == listid:
                name = shoplist.name #temporary workaround
    return render_template('editlist.html', name=name)

@FLASK_APP.route('/shopping-list/<int:listid>/items')
def shopping_list_items(listid):
    """
    View shopping list items
    """
    user = CURRENT_USER['logged_user']
    current_list = None
    shop_list = user.shopping_lists
    for shoplist in shop_list:
        if shoplist.listid == listid:
            current_list = shoplist
    list_name = current_list.name
    return render_template('shoppingitems.html', id=current_list.listid, items=current_list.items, list_name=list_name)

@FLASK_APP.route('/shopping-list/<int:listid>/additems', methods=['POST'])
def add_shopping_list_items(listid):
    """
    view to add shopping items to the shopping list
    """
    user = CURRENT_USER['logged_user']
    user_list = user.shopping_lists
    current_list = None
    for lst in user_list:
        if lst.listid == listid:
            current_list = lst

    if current_list.items == []:
        uid = 1
    else:
        uid = len(current_list.items)+1

    name = request.form['item']
    new_item = Item(uid, name)
    current_list.add_item(new_item)
    return redirect(url_for('shopping_list_items', listid=listid))

@FLASK_APP.route('/shopping-list/<int:listid>/<int:itemid>/edit', methods=['GET', 'POST'])
def edit_shopping_list_item(listid, itemid):
    """
    View to edit item name
    """
    user = CURRENT_USER['logged_user']
    user_list = user.shopping_lists
    current_list = None
    current_item = None
    for lst in user_list:
        if lst.listid == listid:
            current_list = lst
    for item in current_list.items:
        if item.itemid == itemid:
            current_item = item
    if request.method == "POST":
        current_item.update_item(request.form['listname'])
        return redirect(url_for('shopping_list_items', listid=current_list.listid))
    else:
        return render_template('formedit.html', listid=current_list.listid, itmid=current_item.itemid, name=current_item.name)

@FLASK_APP.route('/shopping-list/<int:listid>/<int:itemid>/delete')
def delete_shopping_list_item(listid, itemid):
    """
    view to delete items from shopping list
    """
    user = CURRENT_USER['logged_user']
    user_list = user.shopping_lists
    current_list = None
    current_item = None
    for lst in user_list:
        if lst.listid == listid:
            current_list = lst
    for item in current_list.items:
        if item.itemid == itemid:
            current_item = item
    current_list.delete_item(current_item)
    return redirect(url_for('shopping_list_items', listid=current_list.listid))


if __name__ == '__main__':
    FLASK_APP.run(debug=True)
