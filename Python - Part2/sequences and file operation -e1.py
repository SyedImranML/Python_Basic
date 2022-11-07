# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:21:01 2022

@author: hp
"""

list1 = ["Hadoop","Python","Andrid"]
print(list1)


print(list1[1])

del(list1[1])
print(list1)

list1[1]="Java2"
print(list1)

del(list1[1])
print(list1)

list1=[1,2,3]

list1.append(20)
print(list1)

list1.append(2)
print(list1)

list1.append(7,8)
print(list1)

list1.append((17,8)) #nested elements
print(list1)

del(list1[6]) #out of range

# if more than one elements use extend

list1.extend(9,99)
print(list1)

list1.extend((9,99)) #autmatically separete elements
print(list1)

list1.extend([9,99]) #autmatically separete elements
print(list1)

list1.extend((9,(99,999)))
print(list1)

list1.extend((9,('Hi',"Hello")))
print(list1)

#adding at aparticular index position

list1.insert(4,'Python')

#deleting based on index number

del(list1[3])

#deleting based on element values


list1.remove(99)

list1.remove((99,999))


#### list inside tuple

tuple1=(4,["Python","Java"],5,(1,2,3,"Data Science"))
print(tuple1)

tuple1[1]

tuple1[1][1]=['Master Class Python']
print(tuple1)

tuple1[1]="AI"
