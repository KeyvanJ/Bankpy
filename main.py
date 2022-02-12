import Database

while True:
    n = input()
    if n == 'close':
        break

    # New Account Sign up
    if n == 'register':
        print('please enter your name:')
        n2 = str(input())
        print('please enter a password:')
        p2 = str(input())
        print('please enter your code:')
        c2 = str(input())
        print('please enter your phone number:')
        pn = str(input())
        print('please enter your email:')
        e1 = str(input())
        info = '(' + n2 + ',' + p2 + ',' + c2 + ',' + pn + ',' + e1 + ')'
        command = 'INSERT INTO User VALUES ' + info + ';'
        print(command)
        Database.Database().insert(command)

    # Account Login
    if n == 'login':
        print('Enter your Code:\n')
        c1 = input()
        print('Enter your Password:\n')
        p1 = input()
        command = 'SELECT FROM User WHERE code=="' + c1 + '" AND password=="' + p1 + '";'
        profile = Database.Database().select(command)
        if type(profile) is dict:
            print('Successfully Logged In!')
        else:
            print('Login Failed!')

    if n == 'create account':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        print("enter the account's number:")
        n1 = input()
        print("enter the account's alias:")
        a1 = input()
        print("enter the account's password:")
        p2 = input()
        print("enter the account's balance:")
        b1 = input()
        info = '(' + n1 + ',' + a1 + ',' + p2 + ',' + c1 + ',' + b1 + ');'
        command = 'INSERT INTO Account VALUES ' + info
        Database.Database().insert(command)

    if n == 'show accounts':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        command = 'SELECT FROM Account WHERE code=="' + c1 + '";'
        l = Database.Database().select(command)
        if len(l) == 0:
            print('You do not have any accounts!')
        for i in l:
            print('You have an account by the alias of ', end='')
            print(i['alias'], end='')
            print(' with account number ', end='')
            print(i['number'],end='')
            print(' which has %s dollars in it.' % i['balance'])

