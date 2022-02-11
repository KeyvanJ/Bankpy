class Database:
    users = []
    accounts = []
    #baseuser = {'username':'', 'password':'', 'code':'', 'phone':'', 'email':''}
    #baseaccount = {'number':'', 'ownercode':'', 'balance':''}
    #def writer(self):


    def insert(self, string):
        stringlist = list(map(str, string.split()))
        stringvalue = (stringlist[4]).split(',')
        stringvalue[0] = stringvalue[0][1:]
        stringvalue[-1] = stringvalue[-1][:-2]
        if stringlist[2] == 'User':
            d = {'username': stringvalue[0], 'password': stringvalue[1], 'code':stringvalue[2], 'phone':stringvalue[3], 'email':stringvalue[4]}
            self.users.append(d)
        if stringlist[2] == 'Account':
            d = {'number':stringvalue[0], 'ownercode':stringvalue[1], 'balance':stringvalue[2]}
            self.accounts.append(d)

    def delete(self, string):
        stringlist = list(map(str, string.split()))
        print(stringlist)
        if stringlist[2] == 'User':
            if stringlist[4][0] == 'u' and stringlist[6][0] == 'p':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'p':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['phone'] == f2:
                            self.users.pop(i)

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'c':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][7:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'c':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][7:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['code'] == f2:
                            self.users.pop(i)

            if stringlist[4][0] == 'u' and stringlist[6][0] == 'e':
                f1 = stringlist[4][11:-1]
                f2 = stringlist[6][8:-2]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)

            if stringlist[6][0] == 'u' and stringlist[4][0] == 'e':
                f1 = stringlist[6][11:-2]
                f2 = stringlist[4][8:-1]
                if stringlist[5] == 'OR':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)
                if stringlist[5] == 'AND':
                    for i in self.users:
                        if i['username'] == f1 or i['email'] == f2:
                            self.users.pop(i)

    def update(self, string):
        stringlist = list(map(str, string.split()))
        #print(stringlist)
        stringdel = 'DELETE FROM ' + stringlist[1] + ' WHERE ' + stringlist[3] + ' ' + stringlist[4] + ' ' + stringlist[5] + ';'
        #print(stringdel)
        Database().delete(stringdel)
        stringadd = 'INSERT INTO ' + stringlist[1] + ' VALUES ' + stringlist[7]
        #print(stringadd)
        Database().insert(stringadd)


#Database().insert('INSERT INTO User VALUES (Ali,1234,0441026869,09396096933,ali@yahoo.com);')
#Database().delete('DELETE FROM User WHERE username=="eminem" OR phone=="09396096933";')
Database().update('UPDATE User WHERE username=="eminem" OR phone=="09396096933" VALUES (Mani,5678,2970390140,09122371400,mani@yahoo.com);')


