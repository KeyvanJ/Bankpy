f = open('schema.txt', 'r')
a = f.readlines()
for i in range(len(a)):
    a[i] = a[i][:len(a[i])-1]
p = 0
for i in range(len(a)):
    if a[i] != '':
        k = open('%s.csv' % a[p], 'a+')
        if i != p:
            tmp = list(map(str, a[i].split()))
            k.write(tmp[0])
            k.write(' ')
    if a[i] == '':
        p = i+1
