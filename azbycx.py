s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
l=l1 if l1>l2 else l2
res=""
s2=s2[::-1]
for i in range(l):
    if i<l1:
        res=res+s1[i]
    if i<l2:
        res=res+s2[i]
print(res)
