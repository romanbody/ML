from itertools import product

K,M = map(int,input().split())

'''
k,m = map(int,input().split())
res = 0
for _ in range(k):
    Ki = list(map(int,input().split()))
    Ki2 = list(map(lambda x: x**2, Ki))
    res += max(Ki2)
    print(Ki2)
print(res % m)
'''

N = (list(map(int, input().split()))[1:] for _ in range(K))
print(list(N))
N1 = product(*N)
print(N1)
results = map(lambda x: sum(i**2 for i in x)%M, N1)

print(max(results))
