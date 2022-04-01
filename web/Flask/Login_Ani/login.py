from flask import Flask, session, request, render_template, url_for, redirect

from users import get_user_by_username

from users import add_new_user

app = Flask(__name__)
app.secret_key = b'abc'


@app.route('/')
def home():
    if session.get('user'):
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('profile'))
    form_data = {}
    errors = {}

    if request.method == 'GET':
        return render_template('login.html', form_data=form_data, errors=errors)

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
            return render_template('login.html', errors=errors, form_data=form_data), 400

        session['user'] = {'id': user['id'], 'username': user['username']}

        return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    current_user = session.get('user')
    if not current_user:
        return redirect(url_for('login'))
    return render_template('profile.html', current_user=current_user)


@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
    return redirect(url_for('login'))


@app.route('/signup', methods=['Get', 'Post'])
def signup():
    if session.get('user'):
        return redirect(url_for('profile'))
    form_data = {}
    errors = {}
    if request.method == 'GET':
        return render_template('login.html', form_data=form_data, errors=errors)

    if request.method == 'POST':
        form_data = request.form
        username = form_data.get('username')
        password = form_data.get('password')
        confirm_password = form_data.get('confirm_password')
        if username == '':
            errors['username'] = 'Username is required.'

        if password == "":
            errors['password'] = 'Password is required.'

        if confirm_password == "":
            errors['confirm_password'] = 'Please confirm your password.'

        if confirm_password != password:
            errors['confirm_password'] = 'Passwords is incorrect, please enter passwords again'

        if len(password) < 6:
            errors['password'] = 'Weak password'

        if len(errors) == 0:
            user = add_new_user(username, password)
            session['user'] = {'id': user['id'], 'username': user['username']}
            return redirect(url_for('login'))
    return render_template('signup.html', errors=errors, form_data=form_data), 400


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

# չի ստացվում ստուգել,  login.html-ը չի տեսնում