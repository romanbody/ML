from collections import defaultdict
A = defaultdict(list)

n,m = map(int,input ().split())


[A[input()].append(i+1) for i in range(n)]

for j in [' '.join(map(str, A[input()])) or -1 for i in range(m)]: 
    print (j)
