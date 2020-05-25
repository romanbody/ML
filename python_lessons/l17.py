def check_cube(cubes):
    l = 0 
    r = len(cubes)-1
    last = max (int(cubes[l]),int(cubes[r]))
    while (l<r):
        if cubes[l] == cubes[r]:
            print("left")
            l = l + 1
        else:
            if int(cubes[l]) > int(cubes[r]) and int(cubes[l]) <= int(last):
                last = cubes[l]
                l = l + 1
            else:
                if int(cubes[l]) < int(cubes[r]) and int(cubes[r]) <= int(last):
                    last = cubes[r]
                    r = r - 1
                else:
                    return "No"
    return "Yes"

T = int(input())

cuber = []

for i in range(T):
    xx = int(input())
    cuber.append(check_cube(input().split()))
for i in range(T):
    print(str(cuber[i]))


'''
for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"
'''