#new string in the middle of given string
s1=input()
s2=input()
mi=int(len(s1)/2)
x=s1[:mi:]
x=x+s2
x=x+s1[mi:]
print(x)

 
