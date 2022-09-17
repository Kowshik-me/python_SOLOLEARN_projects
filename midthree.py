#middle three characters
str1=input()
mi = int(len(str1) / 2)
print(str1[mi - 1:mi + 2])
    
 #first mid and last made string"
str1=input()
res=str1[0]
l=len(str1)
mi=int(l / 2)
res = res + str1[mi]
res = res + str1[l - 1]
print(  res)


