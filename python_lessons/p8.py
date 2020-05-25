from itertools import groupby
from collections import UserList
from collections import Counter

class OrderedCounter(Counter):
    pass

#s = input()
s = 'caabbbccde'
s1 = sorted(s)

s2 = UserList()

for x,k in groupby(s1):
    l = list(k)
    s2.append([x,len(l)])
#print(s2)
#s3 = sorted(s2,key=lambda x:x[1],reverse = True)
s3 = sorted(s)
print(s3)

s4 = OrderedCounter(s4)
print(*s4)
s5 = s4.most_common(3)
print(*s5)
#print(s3)
for j in range(3):
    #print(*s3[j]) 
    pass

'''
from collections import Counter

class OrderedCounter(Counter):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
'''