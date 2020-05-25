from itertools import groupby

S = input()
'''
S = '1333211'

for k,c in groupby(S):
    print (int(k),list(c))
'''

#print([(len(list(c)), int(k)) for k, c in groupby(input())])

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

'''
a_list = [("Animal", "cat"),  
          ("Animal", "dog"),  
          ("Bird", "peacock"),  
          ("Bird", "pigeon"),
          ("Animal", "lion"),  
          ("Animal", "tiger")          
          ] 
  
  
an_iterator = groupby(sorted(a_list,key=lambda xx: xx[0]), lambda x : x[0]) 
  
for key, group in an_iterator: 
    li = list(group)
    key_and_group = {key : li} 
    print(key)
    print(len(li))
    print(key_and_group)
'''