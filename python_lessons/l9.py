#s = input ()
s = str("banana").lower()


p1 = "Kevin"
p2 = "Stuart"


pc1 = 0
pc2 = 0

for i in range(0,len(s)-1):
    for j in range(i+1,len(s)+1):
        word = s[i:j]
        #print(word)
        #print (s[i:i+1])
        if s[i:i+1] == "a" or s[i:i+1]=="e" or  s[i:i+1]=="i" or  s[i:i+1]=="o" or  s[i:i+1]=="u":
            pc1 = pc1 + s.count(word)
        else:
            print (word)
            print (s.count(word))
            pc2 = pc2 + s.count(word)

print (pc1)
print (pc2)
if word in s:
    print(s.count(word))
    

s = input().upper()
vowels, L = 'AEIOU', len(s)
K = sum([L-i for i in range(L) if s[i] in vowels])
S = sum([L-i for i in range(L) if s[i] not in vowels])
print(['Stuart '+str(S),['Kevin '+str(K),'Draw'][K==S]][K>=S])    