from itertools import groupby
k=[list(g) for k, g in groupby('AAAABBBCCD')]
print(k)
for i in k:
    newlist=[]
    newlist.append(len(i))
    newlist.append(i[0])
    print(tuple(newlist), end =" ")
