'''
import re

n = int(input())
out = []

for _ in range(n):
    out.append (re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

for i in range(n):
    print(out[i])

'''

import re
for _ in range(int(input())):
    print(re.sub(r' [|]{2}(?= )', ' or', re.sub(r' [&]{2}(?= )', ' and', input())))    