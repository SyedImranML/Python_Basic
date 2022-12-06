##########  FUnctions    ############

def add(n1,n2):
    print(n1,n2)
    return(n1+n2)

op=add('100','200')
    
add(22,2) 


op=add((5,90),(150,90))  


a1=int(input('Enter first number :'))
a2=int(input('Enter second number :'))

op=add(a1,a2)  


# functionis capable of accepting two inputs parameter.

def new(a,b,c,y):
    return b

def third():
    pass

val=new(11,21,8,9)
val2=third()


def abs(n1,n2):
    pass

abs(10,20)

hi=abs(10,20)



def add(n1,n2):
    print(n1,n2)
    file1=open('file1.txt','a')
    file1.write(str(n1+n2))
    file1.close()
    
    
    
op1=add('100','str2')


def add(n1,n2):
    print(n1,n2)
    file1=open('file1.txt','a')
    file1.write(str(n1+n2))
    return n1+n2 if n1>n2 else n2-n1


op=add(100,200)


def add(n1,n2):
    print(n1,n2)
    file1=open('file1.txt','a')
    file1.write(str(n1+n2))
    return n1+n2 if n1>n2 else n2-n1


op=add(200,100)


    
#python | dir() function is a powerful inbuild function in python
#which returns list of the attributes and methods of any object
#say functions,modules,string,list dictionaries  etc...)

dir()

abs(-10)

chr(65)    

chr(97)    

sum([20,30,40000,100])

list(reversed([10,40,30,7,'ji','hi']))

names=['python','steve','jobs']

all(names)

sorted(names,reverse=True)

sorted(names,reverse=False)

import builtins

dir(builtins)
