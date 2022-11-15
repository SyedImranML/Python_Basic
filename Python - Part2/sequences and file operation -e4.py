list1=["Hadoop","Python","Android"]
list1[1]

del(list1[1])

list1[1]="Java2"
print(list1[1])

del(list1[1])
print(list1)


list1=[1,2,3]
list1.append(20)

list1.append(2)

list1.append(7,8)  #append will take single element as an input
list1.append((7,8))
print(list1)

del(list1[6])

list1.append(['Hi','Hello'])
print(list1)

list1.extend(9,999)
list1.extend((99,999))
list1.extend(9,(99,999))
print(list1)

list1.insert((88,888))
list1.insert(4,'Python')
print(list1[1]=var)
print(list1[1])

list1.remove(999)   #based on values


#################Variables

A=10
del(A)

#int,string,float are immutable datatypes

A=10
A=12          #redefining or redeclaring the variable
A=A+2

A="hello"
a='20'
B=10.650908
C=10+6j
del(c)
c=12
print(A,B,C)

c="20"
A='Training'
c=a+A
print(c)

del A
del(B,C)


################# String

str1='hello''welome'
str2="The time is 6'0 Clock"
str3="""Hello'|"O"""
len(str1)

str4='hello how are you \n Good'
print(str4)

str5=r'hello how are you \n Good'  #extended parameter
print(str5)


int=''
del str1
string="Jupyter"
print(string)


x,y,z=100,'20',30
print(x,y,z)


string="Jupyter"
string[:50]

string[0:4] + string[6:10]             #python is a high levelprograming language it always make your code succed


fgh=string[2:]
print(fgh)

print(string[0:5])
len0=len(string)
print(len(string))
var=len(string)
print(string[1:500])

#membership operator
print('z' in string)
print('y' in string)
