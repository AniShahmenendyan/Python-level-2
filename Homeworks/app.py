import psycopg2
import sys
import hashlib

conn = psycopg2.connect("dbname=books_app user=postgres password=postgres host=127.0.0.1")
cur = conn.cursor()
print(sys.argv)


# register
# login
# add
# favorites
# books
def books_view(books):
    print('=' * 50)
    print('Book ID'.ljust(10), 'Name'.ljust(35), 'Author'.ljust(25))
    for book in books:
        book_id, name, author = book
        print(str(book_id).ljust(10), name.ljust(35), author.ljust(25))
    print('=' * 50, '\n')


def execute_and_get_all(sql, params=None):
    if params is None:
        params = ()

    try:
        cur.execute(sql, params)
        return cur.fetchall()
    except:
        conn.rollback()


def execute(sql, params=None):
    if params is None:
        params = ()

    try:
        cur.execute(sql, params)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def add_to_favorites(book_id, user_id):
    sql = """
    INSERT INTO favorites (book_id, user_id) VALUES (%s, %s)
    """

    return execute(sql, (book_id, user_id))


def remove_favorites(book_id, user_id):
    sql = """
    DELETE FROM favorites WHERE book_id = %s AND user_id = %s
    """

    return execute(sql, (book_id, user_id))


def get_favorites(user_id):
    sql = """
    SELECT books.id, books.name, books.author
    FROM favorites 
    LEFT JOIN books on books.id = favorites.book_id 
    WHERE favorites.user_id = %s
    """

    return execute_and_get_all(sql, (user_id,))


def add_user(firstname, lastname, email, password):
    # password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    sql = """
        INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)
        """
    return execute(sql, (firstname, lastname, email, password))


def signup():
    email = ''
    while email == '':
        email = input('Please type your email: \n')
    password = ''
    while password == '':
        password = input('Please type your password: \n')
    firstname = ''
    while firstname == '':
        firstname = input('Please type your firstname: \n')
    lastname = ''
    while lastname == '':
        lastname = input('Please type your lastname: \n')

    user_added = add_user(firstname, lastname, email, str(password))
    if user_added:
        print('User has been signed up successfully!!!')
    else:
        print('Something went wrong!!!')


def login():
    email = ''
    while email == '':
        email = input('Please insert your email \n')
    password = ''
    while password == '':
        password = input('Please insert your password \n')
    try:
        cur.execute('select email from users where password=%s;', (str(password),))
        loged_email = cur.fetchone()[0]
        print(loged_email)
        cur.execute('select id from users where email=%s;', (loged_email,))
        user_id = cur.fetchone()[0]
        print(user_id)
        if loged_email != email:

            print('Invalid username or password,please  try again')



        else:
            while True:
                allowed_commands = ['add', 'remove', 'books', 'favorites', 'logout']

                print('Type books to see all available books.')
                print('Type favorite to see all favorite books.')
                print('Type add to add the book to favorite books.')
                print('Type remove to delete the book from favorite books.')
                print('Type logout to logout.\n')

                command_msg = f'Type [{",".join(allowed_commands)}]: '
                command = input(command_msg)
                command = command.strip()

                while command not in allowed_commands:
                    print('No such command!\n')
                    command = input(command_msg)

                if command in allowed_commands:
                    if command == 'books':
                        cur.execute('select * from books')
                        print('=================================================')
                        cur.copy_to(sys.stdout, 'books', sep='\t')
                        print('=================================================')

                    elif command == 'favorites':

                        cur.execute('select count(user_id) from favorites where user_id = %s', (user_id,))
                        res = cur.fetchone()[0]

                        if res == 0:
                            print('No favorites books. Type add to add them')
                            print('*' * 50)
                        else:
                            favorites = get_favorites(user_id)
                            print('=================================================')
                            books_view(favorites)
                            print('=================================================')
                    if command == 'add':
                        book_id = ''

                        while book_id == '':
                            book_id = input('Please type book id: \n')
                        added = add_to_favorites(book_id, user_id)
                        if added:
                            print('Book was added to favorite list.\n')
                        else:
                            print('Book ID was incorrect or it was already in your favorite list.')
                    elif command == 'remove':
                        book_id = ''
                        while book_id == '':
                            book_id = input("Please type book id: \n")
                        removed = remove_favorites(book_id, user_id)
                        if removed:
                            print('Book was removed from favorite list.\n')
                        else:
                            print('Book ID was incorrect.')
                    elif command == 'logout':
                        print('bye!')
                        sys.exit(1)
    except:
        print('Invalid username or password,please  try again')



if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'signup':
        signup()


    elif len(sys.argv) == 2 and sys.argv[1] == 'login':
        login()
