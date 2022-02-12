import json
import csv
import pandas as pd
import datetime
import os

class Database:
    users = []
    accounts = []
    admins = []
    lists = []
    # baseuser = {'username':'', 'password':'', 'code':'', 'phone':'', 'email':''}
    # baseaccount = {'alias':'', 'password':'', 'ownercode':'', 'balance':''}
    # baseadmin = {'username':'', 'password':''}
    # baselist = {'from':'', 'to':'', 'amount':'', 'time':''}
    def __init__(self):
        with open('User.csv') as csvfile:
            csvread = csv.DictReader(csvfile)
            for row in csvread:
                del row['']
                if row not in self.users:
                    self.users.append(row)

        with open('List.csv') as csvfile:
            csvread = csv.DictReader(csvfile)
            for row in csvread:
                del row['']
                if row not in self.lists:
                    self.lists.append(row)

        with open('Admin.csv') as csvfile:
            csvread = csv.DictReader(csvfile)
            for row in csvread:
                del row['']
                if row not in self.admins:
                    self.admins.append(row)

        with open('Account.csv') as csvfile:
            csvread = csv.DictReader(csvfile)
            for row in csvread:
                del row['']
                if row not in self.accounts:
                    self.accounts.append(row)

        dydx = {'username': 'Keyvan', 'password': '3658'}
        if dydx not in self.admins:
            self.admins.append(dydx)

    def write(self):
        os.remove('User.csv')
        os.remove('User.json')
        with open('User.json', 'w') as f:
            json.dump(self.users, f)
        df = pd.read_json('User.json')
        df.to_csv('User.csv')

        os.remove('Admin.json')
        os.remove('Admin.csv')
        with open('Admin.json', 'w') as f:
            json.dump(self.admins, f)
        df = pd.read_json('Admin.json')
        df.to_csv('Admin.csv')

        os.remove('List.json')
        os.remove('List.csv')
        with open('List.json', 'w') as f:
            json.dump(self.lists, f)
        df = pd.read_json('List.json')
        df.to_csv('List.csv')

        os.remove('Account.json')
        os.remove('Account.csv')
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
            elif len(stringvalue[2]) > 12 or type(stringvalue[2]) is not str:
                print('Code e Melli is not Correct!')
            # Phone Check
            elif len(stringvalue[3]) > 13 or type(stringvalue[3]) is not str:
                print('Phone Number is not Correct!')
            # Email Check
            elif len(stringvalue[4]) > 64:
                print('Email is too long!')
            elif type(stringvalue[4]) is not str:
                print('Email must only contain characters!')
            else:
                d = {'username': stringvalue[0], 'password': str(stringvalue[1]), 'code': str(stringvalue[2]), 'phone': str(stringvalue[3]), 'email': stringvalue[4]}
                self.users.append(d)
                Database().write()
                print('Sign Up Successful!')
        if stringlist[2] == 'Account':
            d = {'number': str(stringvalue[0]), 'alias': stringvalue[1], 'password': str(stringvalue[2]), 'ownercode': str(stringvalue[3]), 'balance': str(stringvalue[4])}
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
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.remove(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'p':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.remove(i)
                            Database().write()

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'c':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][7:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.remove(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'c':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][7:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.remove(i)
                            Database().write()

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'e':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.remove(i)
                            Database().write()

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'e':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.remove(i)
                            Database().write()
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.remove(i)
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
        if stringlist[2] == 'Account':
            if stringlist[4][0] == 'c':
                f1 = stringlist[4][7:-2]
                d = []
                for i in self.accounts:
                    if i['ownercode'] == f1:
                        d.append(i)
                return d
            if stringlist[4][0] == 'n':
                f1 = stringlist[4][9:-2]
                for i in self.accounts:
                    if i['number'] == f1:
                        return i

        if stringlist[2] == 'List':
            f1 = stringlist[4][9:-2]
            d = []
            for i in self.lists:
                if i['from'] == f1 or i['to'] == f1:
                    d.append(i)
            return d






# Database().insert('INSERT INTO User VALUES (Ali,1234,0441026869,09396096933,ali@yahoo.com);')
# Database().delete('DELETE FROM User WHERE username=="Ali" OR phone=="09396096933";')
# Database().update('UPDATE User WHERE username=="eminem" OR phone=="09396096933" VALUES (Mani,5678,2970390140,09122371400,mani@yahoo.com);')
# Database().select('SELECT FROM User WHERE code=="0441026869" AND password=="1234";'))
# Database().select('SELECT FROM Account WHERE code=="0441026869";')
# print(Database.users)
