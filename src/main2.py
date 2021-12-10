a=1
print(a)

import cmath
import math

c=math.cos(math.pi)
print(c)

d=27
type(d)
print(d)
#<type 'int'>
#if(d):
#print(True)

var1 = 'Hello World!'
var2 = "Python Programming"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])


a = "Hello"
c= a+a+a                        #concatenazione
print(c)

a = "He"+"l"*2+"o World"        #concatenazione multipla
print(a)

a = "What’s your name?" # Ok if I create the string with double quotes
b = "What\’s your name?"  # Ok if you escape the single quote character
print (a)
print(b)

a = r"Hello \t World"
#Raw string
print(a)
 
name = "karin"
my_string = "ciao %s" % name # Append and Insert
my_string = "ciao %s, come stai? %s" % (name, 'tutto bene, grazie') # Insert multiple values
print(my_string)

person = {"name": "karin", "age": 21}
print(f"{person['name']} is {person['age']} years old.")

s="Ciao a tuttiiii"
d=s.replace('o','i',1)
print(d)

s = "Hello"
d=s.center(10,'.')
print(d)

d=s.upper()
print(d)