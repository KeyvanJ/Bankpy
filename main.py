import Database

while True:
    n = input()
    if n == 'close':
        break

    # New Account Sign up
    if n == 'register':
        print('Please enter your name:')
        n2 = str(input())
        print('Please enter a password:')
        p2 = str(input())
        print('Please enter your code:')
        c2 = "'" + str(input()) + "'"
        print('Please enter your phone number:')
        pn = "'" + str(input()) + "'"
        print('Please enter your email:')
        e1 = str(input())
        info = '(' + n2 + ',' + p2 + ',' + c2 + ',' + pn + ',' + e1 + ')'
        command = 'INSERT INTO User VALUES ' + info + ';'
        Database.Database().insert(command)

    # Profile Login
    if n == 'login':
        print('Please enter your Code:')
        c1 = "'" + input() + "'"
        print('Please enter your Password:')
        p1 = input()
        command = 'SELECT FROM User WHERE code=="' + c1 + '" AND password=="' + p1 + '";'
        profile = Database.Database().select(command)
        if type(profile) is dict:
            print('Successfully Logged In!')
        else:
            print('Login Failed!')

    # Account Addition
    if n == 'add account':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        print("Please enter the account's number:")
        n1 = input()
        print("Please enter the account's alias:")
        a1 = input()
        print("Please enter the account's password:")
        p2 = input()
        print("Please enter the account's balance:")
        b1 = input()
        info = '(' + n1 + ',' + a1 + ',' + p2 + ',' + c1 + ',' + b1 + ');'
        command = 'INSERT INTO Account VALUES ' + info
        Database.Database().insert(command)
        print('Account added!')

    # Accounts Display
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
            print(i['number'], end='')
            print(' which has %s dollars in it.' % i['balance'], '\n')

    # Money Transfer
    if n == 'transfer':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        print('Please enter the account number you want to transfer from:')
        fr1 = input()
        print('Please enter account password:')
        p2 = input()
        command = 'SELECT FROM Account WHERE number=="' + fr1 + '";'
        acc = Database.Database().select(command)
        if p1 != acc['password']:
            print('Incorrect Password!')
        else:
            print('Please enter the account number you want to transfer to:')
            to1 = input()
            print('Please enter the amount you want to transfer:')
            am1 = input()
            info = '(' + fr1 + ',' + to1 + ',' + am1 + ');'
            command = 'INSERT INTO List VALUES ' + info
            Database.Database().insert(command)
            info = '(' + to1 + ',' + fr1 + ',' + am1 + ');'
            command = 'INSERT INTO List VALUES ' + info
            Database.Database().insert(command)
            acc['balance'] = int(acc['balance']) - int(am1)
            command = 'SELECT FROM Account WHERE number=="' + to1 + '";'
            acc = Database.Database().select(command)
            acc['balance'] = int(acc['balance']) + int(am1)
            print('Transfer successful!')

    # Transaction List
    if n == 'transactions':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        print('Please enter the account you want its list of transactions:')
        ac1 = input()
        print('Please enter account password:')
        p2 = input()
        command = 'SELECT FROM Account WHERE number=="' + ac1 + '";'
        acc = Database.Database().select(command)
        if p2 != acc['password']:
            print('Incorrect Password!')
        else:
            command = 'SELECT FROM List WHERE number=="' + ac1 + '";'
            l = Database.Database().select(command)
            print('Transactions:')
            for j in l:
                print('Transaction of %s dollars' % l['amount'], end='')
                print(' from ', l['from'], ' to ', l['to'], ' at ', l['time'],'\n')

    # Paying bills
    if n == 'pay bills':
        if type(profile) is not dict:
            print('You are not logged in yet!')
            break
        print('Please enter the account you want to use to pay bills:')
        ac1 = input()
        print('Please enter account password:')
        p2 = input()
        command = 'SELECT FROM Account WHERE number=="' + ac1 + '";'
        acc = Database.Database().select(command)
        if p2 != acc['password']:
            print('Incorrect Password!')
        else:
            print('Please enter the serial number of the bill you want to pay:')
            b1 = input()
            print('Please enter the price of the bill:')
            am2 = input()
            acc['balance'] = int(acc['balance']) - int(am2)
            print('Payment successful!')

    # Admin Panel
    if n == 'admin login':
        print('Please enter your username:')
        adu = input()
        print('Please enter your password:')
        adp = str(input())
        command = 'SELECT FROM Admin WHERE username=="' + adu + '";'
        prof = Database.Database().select(command)
        if prof['password'] == adp:
            print('Admin successfully logged in!')
            while True:
                m = input()
                if m == 'close panel':
                    break


        else:
            print('Login failed.')

