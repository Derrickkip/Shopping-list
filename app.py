from flask import Flask, render_template, request, flash, redirect, url_for, session
from classes import User

SECRET_KEY = 'NaughtyNaughty'

app = Flask(__name__, template_folder='Designs', static_folder='Designs/static')
app.config.from_object(__name__)

UserList = {}


@app.route('/')
def home():
    """
    Home page view
    """
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    User registration view
    """
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['passwd']
        if UserList == {}:
            uid = 1
        else:
            uid = len(UserList.items())+1
        if password != password2:
            flash('Passwords do not match')
            render_template('registration.html')
        user = {
            'uid': uid,
            'username': username,
            'password':password
        }
        UserList[email] = user
        flash('Registration success')
        return redirect(url_for('login'))
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    User Login view
    """
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in UserList or password != UserList[email]['password']:
            error = 'Invalid username or password. Please try again!'
        else:
            flash("You were successfully logged in")
            session['logged_in'] = True
            return redirect(url_for('shopping_list'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """
    View to log user out of the app
    """
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

@app.route('/shopping-list')
def shopping_list():
    """
    view for showing shooping lists
    """
    users = UserList
    return render_template('shoppinglist.html', user = users)


if __name__ == '__main__':
    app.run(debug=True)
