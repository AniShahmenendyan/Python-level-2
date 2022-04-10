from flask import Flask, session, request, render_template, url_for, redirect
from functools import wraps
from users import get_user_by_username, add_new_user
from password import hash_password

app = Flask(__name__)
app.secret_key = b'abc'


@app.context_processor
def inject_user():
    current_user = session.get('user')
    return dict(current_user=current_user)


def require_anonymous(function):
    @wraps(function)
    def inner(*args, **kwargs):
        if session.get('user'):
            return redirect('profile')
        return function(*args, **kwargs)

    return inner


def require_login(function):
    @wraps(function)
    def inner(*args, **kwargs):
        if not session.get('user'):
            return redirect('login')
        return function(*args, **kwargs)

    return inner

@app.route('/')
@require_login
def home():
    # if session.get('user'):
    #     return redirect(url_for('profile'))
    # else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
@require_anonymous
def login():
    # if session.get('user'):
    #     return redirect(url_for('profile'))
    form_data = {}
    errors = {}

    if request.method == 'GET':
        return render_template('/login.html', form_data=form_data, errors=errors)

    if request.method == 'POST':
        form_data = request.form
        username = form_data.get('username')
        password = form_data.get('password')

        if not username:
            errors['username'] = 'Username is required.'

        if not password:
            errors['password'] = 'Password is required.'

        if len(errors) == 0:
            user = get_user_by_username(username)

            if user is None:
                errors['form_error'] = 'Invalid credentials.'

            if user is not None:
                if password != user['password']:
                    errors['form_error'] = 'Invalid credentials.'

        if len(errors):
            return render_template('/login.html', errors=errors, form_data=form_data), 400

        session['user'] = {'id': user['id'], 'username': user['username']}

        return redirect(url_for('profile'))


@app.route('/profile')
@require_login
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
    return redirect(url_for('login'))


@app.route('/signup', methods=['Get', 'Post'])
@require_anonymous
def signup():
    form_data = {}

    # if session.get('user'):
    #     return redirect(url_for('profile'))
    errors = {}
    if request.method == 'GET':
        return render_template('/signup.html', form_data=form_data, errors=errors)

    if request.method == 'POST':
        form_data = request.form
        username = form_data.get('username')
        password = form_data.get('password')
        confirm_password = form_data.get('confirm_password')
        if not username:
            errors['username'] = 'Username is required.'

        if not password:
            errors['password'] = 'Password is required.'

        if not confirm_password:
            errors['confirm_password'] = 'Please confirm your password.'

        if password and confirm_password != password:
            errors['confirm_password'] = "Passwords don't match, please enter passwords again!"

        if len(errors) == 0 and len(password) < 6:
            errors['password'] = 'Weak password'



        if len(errors) == 0:
            user = get_user_by_username(username)
            if user:
                errors['username'] = "Username is already in use"
            else:
                hash_password(password)
                add_new_user(username, password)

                return redirect(url_for('login'))
    return render_template('/signup.html', errors=errors, form_data=form_data), 400


if __name__ == "__main__":
    app.run(debug=True)

