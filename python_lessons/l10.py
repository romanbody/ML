
[print(*(list(range(1,j+1)) + list (range(j-1,0,-1))), sep='') for j in range (1,int(input())+1)]
'''
for i in range(int(input())):
    out1 = ""
    [out1 ++ str(j+1) for j in range(i+1)]
    [out1 ++ str(j) for j in range(i,0,-1)]
    print(out1)
'''
for i in range(1,int(input())+1): print(pow(((pow(10,i)-1)//9),2))

'''
5
1
121
12321
1234321
123454321
5
1
121
12321
1234321
123454321
'''