# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 23:04:06 2022

@author: hp
"""

### Python Operators

#Arithematic Operators
a=50
b=45

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #modulus
print(a//b) #floor division
print(a**3) #exponentiation

'hi ' + 'how r u'
hi='hi ' + 'how r u'


#Assignment Operator

a=30
30=a
b=1
a=c
c=a
print(a)


b=10
a=a+b
a+=b
print(a)

a=a+b

a=a-b
a-=b
print(a)

a*=b
print(a)

a/=b
print(a)

a=a**b
a**=b
print(a)

a//=b
print(a)



#Comparision Operator

a=50
b=100
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


#membership operator

list1=[1,10,100,10,"Data Science"]
print(10in list1)


print('Data Science'not in list1)
print("Data Science" not in list1)
print('Data Science' in list1)

var1=['a','b','c']
var2=['b','c']

print(var2[0:2] in var1)

for i in range(2):
    print(i)
print(var2[i] in var1)

### Conditional Operator

x=20
y=15

if x<y:
    print('X is greater than Y')
    
print('X is not less than Y')


if x>y:
    print('X is greater than Y')
  
print('X is not less than Y')

a=5
b=5
c=10
if(x>y & a==b):
    print("true and true")
    print("new line")
    print("new line2")
    
    
X=10
Y=10
if(X<Y):
    print('X is NOT greater than Y')
    print('rgregrg')
elif(X>Y):
    print('X is greater than Y')
elif(X==Y):
    print('X is equal to Y')
else:
    print('Not matching any condition')

X=100
Y=10
if(X<Y):
    print('X is NOT greater than Y')
    print('rgregrg')
elif(X>Y):
    print('X is greater than Y')
elif(X==Y):
    print('X is equal to Y')
else:
    print('Not matching any condition')


X=5
Y=10
if(X<Y):
    print('X is NOT greater than Y')
    print('rgregrg')
elif(X>Y):
    print('X is greater than Y')
elif(X==Y):
    print('X is equal to Y')
else:
    print('Not matching any condition')
    
    
#if else statement

a=25
b=11
if(a==25):
    print("a is 25")
    if(b==10):
        print("b equal to 10")
        print("End")
        
elif(10<=a<=25):
    print("In between 10 and 25")
    if(b==10):
        print("b equal to 10")
        print("End")
else:
    print("Greater than 25")
    
a=15
b=10
if(a==25):
    print("a is 25")
    if(b==10):
        print("b equal to 10")
        print("End")
        
elif(10<=a<=25):
    print("In between 10 and 25")
    if(b==10):
        print("b equal to 10")
        print("End")
else:
    print("Greater than 25")
        
    

