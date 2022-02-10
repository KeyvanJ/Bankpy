class Database:
    users = []
    accounts = []
    #baseuser = {'username':'', 'password':'', 'code':'', 'number':'', 'email':''}
    #baseaccount = {'number':'', 'ownercode':'', 'balance':''}
    def writer(self):


    def insert(self, string):
        stringlist = list(map(str, string.split()))
        stringvalue = (stringlist[4]).split(',')
        stringvalue[0] = stringvalue[0][1:]
        stringvalue[-1] = stringvalue[-1][:-1]
        if stringlist[2] == 'User':
            d = {'username': stringvalue[0], 'password': stringvalue[1], 'code':stringvalue[2], 'number':stringvalue[3], 'email':stringvalue[4]}
            self.users.append(d)
            #print(stringlist)
            #print(stringvalue)
        if stringlist[2] == 'Account':
            d = {'number':stringvalue[0], 'ownercode':stringvalue[1], 'balance':stringvalue[2]}
            self.accounts.append(d)



Database().insert('INSERT INTO User VALUES (Ali,1234,0441026869,09396096933,ali@yahoo.com)')


