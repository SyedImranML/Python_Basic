# Dictionay nested elements - building story  #rec records

rec = {'Name':{'First':'Elon','Last':'Mask'},
       'Jobs':['Engineer','Sr. Engineer','Manager'],
       'Pramotion':(1998,2000,2008),
       'Age':40.5}

rec['Name']='one'
rec['Name']['First']
rec['Name']['First']='Smith'

rec['Jobs'][0]
rec['Jobs'][0]='Developer'

rec['Pramotion'][1]
rec['Pramotion'][1]=2005        #by mistake some can change 

rec['Name']['Last']
rec['Name']['midle']='Will'

del(rec['Name']['midle'])
rec['sal']=250000


################   Sets #############################

# deals only with key L I,V , T - I,L D - K, V S - only K

A={1,3,2,4,3,4,4,3}
A

A.add(('hi',"hello"))
A.add(6)

a='Python'
b="ML"

A.add((a,b))

newset=set([3,4,5,7])
print(newset)

A={1,2,3,4}
B={3,3,4,5,7}

print(A|B)  #or       #unique values in both the sets
print(A&B)  #and      # common in both the sets

A={1,2,4,5,7}         #dedicatedly work in specific
B={4,5,6,7,8}
c={3}

print(A-B)           #dedicatedly work in specific
print(B-A)

c=B-A


#The Python symmetric_difference() method returns 
#the symmetric difference of two sets. The symmetric 
#difference of two sets A and B is the set of elements 
#that are in either A or B , but not in their intersection.
s={'a','b','c','d','e','f','o','v'}
set1={'a','b','d','v'}
set2={'a','c','d','o','e'}
print(set1|set2)
print(set1&set2)
print(set1-set2)


#add

s={1,2,3,'a','c','b'}
set1={1,'a','b'}
print(3  in s)

print(set1.issubset(s))

print(3 not in s)

print(s.issuperset(set1))

print(s.union(set1)) # |

print(s.intersection(set1)) # & 

print(s.difference(set1)) # -


print(s.symmetric_difference(set1))

set_A = {1, 2, 3, 4, 5} 
set_B = {6, 7, 3, 4} 
set_A-set_B
print(set_A.intersection(set_B))
print(set_A.symmetric_difference(set_B)) 
A

