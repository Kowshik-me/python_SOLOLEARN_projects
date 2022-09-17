#count characters digists special characters
str1=input()
cc=0
dc=0
sc=0
for c in str1:
    if c.isalpha():
        cc+=1
    elif c.isdigit():
        dc+=1
    else:
        sc+=1
print(cc,dc,sc)

 
