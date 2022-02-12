import Database

while True:
    n = input()
    if n == 'close':
        break

    # New Account Sign up
    if n == 'register':
        print('Please enter your credentials in the following format: (username,password,code,phone,email)')
        info = input()
        command = 'INSERT INTO User VALUES ' + info + ';'
        Database.Database().insert(command)

    # Account Login
    if n == 'login':
        print('Enter your Code:\n')
        c1 = input()
        print('Enter your Password:\n')
        p1 = input()
        command = 'SELECT FROM User WHERE code=="' + c1 + '" AND password=="' + p1 + '";'
        profile = Database.Database().select(command)
        print(profile)




