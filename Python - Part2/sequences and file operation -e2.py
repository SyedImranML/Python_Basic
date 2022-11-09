tuple1=(4,["Python","Java"],5,(1,2,3,"Data Science"))

tuple1[1][1]='Scala'
#you are modifying the value with in a list and the
# list is present within a tuple
#Note :It doesn't become immutable

# if i am doing the same activity like this
tuple1[1]='Scala'

#Here we are modifying tuple that means you are
#  modifying the structure of tuple.

tuple1[3][1]=30   #double index
# i can'tmodify the values of tuple within the
#tuple because tuple is immutable object.

del(tuple1[1][0])
#you are ableto delete because we are dealing 
# with list

# Dealing with nested elements with same syntax.

tuple1[3][0]=10
tuple1[3]='Hadoop'

# Discussing about Range

tuple1[0:1]

#range values will expect you to generate next
# value based on index.

tuple1[:1]
tuple1[1]
tuple1[1][:1]
tuple1[3][:3]


# Dictionaries   Define with curly braces

#our own Key and our own Value
#Key value pairs

sample=10
A={'Age':90,'FirstName':'Ding','SecondName':'Dong','Gender':'M'}
print(A)
A['Age'] 

#Here there is no concept of index

dict={10:"Python",20:"Android",30:"win"}
print(dict) 

print(dict[40])
#KeyError as no key with this number

dict[40]=('Hadoop')

dict[50]=['new1',80,820]

#key can never be duplicate
# Value can be duplicate or we can have list with
# duplicate values

dict[50]=['new2',80,720]

#Key will always be immutable datatypes.
#key can be of any datatype but it should be immutable.
#What python do is it will only except immutable datatype like integer,string,tuple.

dic={10:"A2",20:"A2",30:"A3",30:"A3_new"}
# the last one will only be active.


dic[30]='new values'  #key with integer type

dic['30']='new_values' #key with string type

dic[('hi',40)]=['new',828,800] #key with tuple type

dic11={1.1:"Python",1.2:"Hadoop"}


d={10:'A1','name':36,4.5:'run'}

#note :mapping is done based on keys only.

# Dictionay is a mutable object

del(dic[10])
