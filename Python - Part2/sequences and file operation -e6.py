string="Jupyter"
print(string)

string[:50]

string[0:4] + string[6:10]


fgh=string[2:]

############ Tuple #####
# tuple is a high level datatypes
# index position starting from zero
# allocation will be indiviual objects

course ="Data Science"
course[0:5]
tup1=("Python","Android","os",course)
tup1[1]
tup1[0:4]
tup1[0:3]

tup1[0:7:2]
tup1[1:7:3]

tup1[1:400]       #will make logic not to get failed

tup1[-1]
tup1[::-1]

len(tup1)
tup1[2:3]

print(len(tup1))
print(max(tup1))
print(min(tup1))


type(tup1)


tup1=("Hadoop","Python","Java",10)
tup1[0][1:6]

print(len(tup1))
print(len(tup1[0]))

print(tup1*3)
print(tup1[0]*2)

print('Python' in tup1)


tup2=(1,3,5,7)
tup3=(2,4,6,8)
tup5=tup2+tup3
print(len(tup5))
print(max(tup5))
print(min(tup5))

type(tup5)

del(tup1)
print(tup1)

tuple1=("c",'a','b')
tuple1[1]
tuple1[1]="Python" #going to fail becauseof immutable datatype

#note : once you create a tuple  you can't modify a tuple
# even if i want to delete also i can't delete the individual elements
#if i want to delete you can delete entire tuple


del(tuple1[1])
del(tuple1) 

tup=(1,3,5,2)
print(sorted(tup))

tuple1=('c','a','b')
tuple1=''
len(tuple1)
lst=list(tuple1)

lst.append('d')
tuple1=tuple(lst)

print(sorted(tuple1))
tuple2=sorted(tuple1)
tuple1=tuple2

#Once you create a tuple we can't modify the existing tuple

print(tuple1)
tuple1[-2]

print(tuple1[-1])
op=tuple1[::-1]
print(sorted(tuple1))
tuple3=sorted(op)


print('Hello World')
print("Welcome to Python")
print('Happy Learning ' + '\n' +'Welcome to Python '+ 'Hello')
print(r'Happy Learning ' + r'\n ' +'Welcome to Python '+ 'Hello')


A=10
atype=type(A)
print(atype)

A=(1,2)
tup2=(1,3,5,7)
tup3=(2,4,6,8)
tup5=tup2+(4,6)
print(tup5)
print(sorted(tup5))
