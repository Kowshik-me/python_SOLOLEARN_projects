#Exponentiation

for i in range(1,31):
    if i==30:
        print(0.01*(2**i))
#........................................................................



#Simple Calculator

x=int(input())
y=int(input())
z=x+y
print(z)
#............................................................................



#FizzBuzz

n = int(input())
 
for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
#.............................................................................



#Celsius to Fahrenheit
 
+13

#You missed the main formula 
celsius = int(input())

def conv(c):
  #your code goes here
     return (c*9/5)+32

fahrenheit = conv(celsius)
print(fahrenheit)

#...............................................................................



#Book Titles
file = open("/usercode/files/books.txt", "r")
 
#your code goes here
fileLines = []
for lines in file:
    fileLines.append(lines)
length = 1
for n in fileLines:
    if length == len(fileLines):
        print(n[0] + str(len(n)))
    else:
        print(n[0] + str(len(n)-1))
    length += 1
file.close()
#........................................................................


#Longest Word
text = input().split()
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text[text_index])
#..............................................................................
 

#Fibonacci
num = int(input())
 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(num):
    print(fibonacci(i))
#................................................................................

#Juice Maker

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
 
    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    
    def __add__(self,newJuice):
        
        self.name += "&" + str(newJuice.name)
        self.capacity += newJuice.capacity 
        return self.__str__

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

print(a.__add__(b)())
#.............................................................................



#Phone Number Validator
import re
#your code goes here
 
number = input()

pattern = r'1|8|9{1}[0-9]'

if re.match(pattern, number) and len(number) == 8:
    print("Valid")

else:
    print("Invalid")
#............................................................................



#Adding Words
def concatenate(*args):
    x = (args)
    print(x[0] + "-" + x[1] + "-" + x[2] + "-" + x[3])
 
concatenate("I", "love", "Python", "!")









									

