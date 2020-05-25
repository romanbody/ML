import itertools

its1 = [range(10)]
its2 = [range(10)]

for x,y,z in itertools.product(*its1,*its2, *its2):
    print(x, y,z)


from itertools import product

a = [1, 2]
b = [4, 5]
c = ["x", "y", "z"]
print(*product(a, b, c))

print(*product(*its1, *its2, *its2))