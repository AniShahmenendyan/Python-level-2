import hashlib
users = [
    {
        'id': 1,
        'username': 'felix',
        'password': '123'
    },
    {
        'id': 2,
        'username': 'flask',
        'password': '123'
    },
]


def get_user_by_username(username=None):
    for user in users:
        if user['username'] == username:
            return user

def add_new_user(username, password):
    new_user = {}
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if username not in users:
        new_user.update({'id': len(users) + 1, 'username': 'username', "password": 'password'})
        users.append(new_user)
        return new_user


