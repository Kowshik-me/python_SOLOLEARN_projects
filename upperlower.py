s=input()
l=[]
u=[]
for char in s:
    if char.islower(): 
        l.append(char)
    else:
        u.append(char)
s=''.join(l+u)
print(s) 
