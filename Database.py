import json
import pandas as pd
import datetime

class Database:
    users = []
    accounts = []
    admins = []
    lists = []
    # baseuser = {'username':'', 'password':'', 'code':'', 'phone':'', 'email':''}
    # baseaccount = {'alias':'', 'password':'', 'ownercode':'', 'balance':''}
    # baseadmin = {'username':'', 'password':''}
    # baselist = {'from':'', 'to':'', 'amount':'', 'time':''}

    def write(self):
        with open('User.json', 'w') as f:
            json.dump(self.users, f)
        df = pd.read_json('User.json')
        df.to_csv('User.csv')

        with open('Admin.json', 'w') as f:
            json.dump(self.admins, f)
        df = pd.read_json('Admin.json')
        df.to_csv('Admin.csv')

        with open('List.json', 'w') as f:
            json.dump(self.lists, f)
        df = pd.read_json('List.json')
        df.to_csv('List.csv')

        with open('Account.json', 'w') as f:
            json.dump(self.accounts, f)
        df = pd.read_json('Account.json')
        df.to_csv('Account.csv')

    def insert(self, string):
        stringlist = list(map(str, string.split()))
        stringvalue = (stringlist[4]).split(',')
        stringvalue[0] = stringvalue[0][1:]
        stringvalue[-1] = stringvalue[-1][:-2]
        if stringlist[2] == 'User':
            # Username check
            if len(stringvalue[0]) > 64:
                print('Username is too long!')
            elif type(stringvalue[0]) is not str:
                print('Username must only contain characters!')
            for i in self.users:
                if i['username'] == stringvalue[0]:
                    print('Username is unavailable')
            # Password check
            if len(stringvalue[1]) > 64:
                print('Password is too long!')
            elif type(stringvalue[1]) is not str:
                print('Password must only contain characters!')
            # Code e Melli check
            elif len(stringvalue[2]) > 10 or type(stringvalue[2]) is not str:
                print('Code e Melli is not Correct!')
            # Phone Check
            elif len(stringvalue[3]) > 11 or type(stringvalue[3]) is not str:
                print('Phone Number is not Correct!')
            # Email Check
            elif len(stringvalue[4]) > 64:
                print('Email is too long!')
            elif type(stringvalue[4]) is not str:
                print('Email must only contain characters!')
            else:
                d = {'username': stringvalue[0], 'password': stringvalue[1], 'code': stringvalue[2], 'phone': stringvalue[3], 'email': stringvalue[4]}
                self.users.append(d)
                Database().write()
                print('Sign Up Successful!')
        if stringlist[2] == 'Account':
            d = {'alias': stringvalue[0], 'password': stringvalue[1], 'ownercode': stringvalue[2], 'balance': stringvalue[3]}
            self.accounts.append(d)
            Database().write()
            print('New Account Added!')
        if stringlist[2] == 'List':
            ttt = datetime.datetime.now().time()
            d = {'from': stringvalue[0], 'to': stringvalue[1], 'amount': stringvalue[2], 'time': ttt}
            self.lists.append(d)
            Database().write()

    def delete(self, string):
        stringlist = list(map(str, string.split()))
        #print(stringlist)
        if stringlist[2] == 'User':
            if stringlist[4][0] == 'u' and stringlist[6][0] == 'p':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'p':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                            Database().write()

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'c':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][7:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'c':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][7:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                            Database().write()

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'e':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'e':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                            Database().write()

    def update(self, string):
        stringlist = list(map(str, string.split()))
        # print(stringlist)
        stringdel = 'DELETE FROM ' + stringlist[1] + ' WHERE ' + stringlist[3] + ' ' + stringlist[4] + ' ' + stringlist[5] + ';'
        # print(stringdel)
        Database().delete(stringdel)
        stringadd = 'INSERT INTO ' + stringlist[1] + ' VALUES ' + stringlist[7]
        # print(stringadd)
        Database().insert(stringadd)

    def select(self, string):
        stringlist = list(map(str, string.split()))
        # print(stringlist)
        if stringlist[2] == 'User':
            if stringlist[4][0] == 'u' and stringlist[6][0] == 'p':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            return i

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'p':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            return i

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'c':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][7:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            return i

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'c':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][7:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            return i

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'e':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            return i

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'e':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            return i
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            return i

            if stringlist[4][0] == 'c' and stringlist[6][0] == 'p':
                f1 = stringlist[4][7:-1]
                f2 = stringlist[6][11:-2]
                for i in self.users:
                    if i['code'] == f1 and i['password'] == f2:
                        return i





# Database().insert('INSERT INTO User VALUES (Ali,1234,0441026869,09396096933,ali@yahoo.com);')
# Database().delete('DELETE FROM User WHERE username=="eminem" OR phone=="09396096933";')
# Database().update('UPDATE User WHERE username=="eminem" OR phone=="09396096933" VALUES (Mani,5678,2970390140,09122371400,mani@yahoo.com);')
# Database().select('SELECT FROM User WHERE code=="0441026869" AND password=="1234";'))
