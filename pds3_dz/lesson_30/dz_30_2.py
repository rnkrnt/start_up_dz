from hashlib import md5


def user_reg():
    user_num = int(input('Enter a number of users to register: '))
    global login_pass_hash
    login_pass_hash = dict()
    for i in range(user_num):
        login = input(f'Enter login for user{i + 1}: ')
        password = input(f'Enter password for user{i + 1}: ')
        login_pass_hash[login] = md5(bytes(password, 'UTF-8')).hexdigest()


def user_auth():
    login = input('Login: ')
    password = input('Password: ')
    try:
        if login_pass_hash[login] == md5(bytes(password, 'UTF-8')).hexdigest():
            print('login successful!')
        else:
            print('login or password is incorrect!')
    except KeyError:
        print('login or password is incorrect!')
