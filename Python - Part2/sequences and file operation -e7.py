############## LOOPS ######
##### While Loop ####
count =0
while(count<=10):
    print(count)
    #count+=1
    count=count+1
    
print("Good Bye !")

#Example 

rank=5
while(rank!=12):
    print("Rank is ",rank)
    rank+=1

##### For Loop

#Example 

list1=(1,2,3,"Python","Java","Scala")

for i in list1:
    print(i)
    
emp=['Syed Imran','david','Danny','John']
for e in emp:
    print('Your bonus ' + e )
    
    
fruits = ['Banana',[1,'a'],'Grapes',7]

for i in fruits[1:]:
    print(type(i))
    print(i)
    
    
fruits = ['Banana',[1,'a'],'Grapes',7]

for i in fruits(1:):        #Error index should always be in []
    print(type(i))
    print(i)
    
for i in range(50):
    print(i)
    
a=range(1,10)
for i in a:
    print(i)
    

for i in range(1,4):
    print(i)
    print(fruits[i])
    
 
    # IndexError: list index out of range
    
for i in range(1,40):
    print(i)
    print(fruits[i])
    
    #better to go with len function
    
for i in range(1,len(fruits)):
    print(i)
    print(fruits[i])


for index in range(1,40):
    print(index)
    
####### Nested loops

count=1
for i in range(0,10):
    print(i)
    for j in range(count,10):
        print(j)
        print('Count ',count)
        count=count+1
        
        
########### Loop control   #######

for i in range(10,50):
    print(i)
    #break
    if(i==30):
        break;

print("Ending Here...")


#######  Continue

for j in range(1,11):
    #continue
    #print(j)
    if(j==5):
        print('Skipped')
        continue
    print(j)
    
    

for j in range(1,11):
    #continue
    #print(j)
    if(j==5):
        print('Skipped')
        continue
    if(j==8):
        print('Skipped')
        continue
    print(j)
  
    
  # Using while loop
  
  count=0
  while(count<=15):
      print(count)
      #count+=1
      print('Count less than 15')
      if(count==10):
          break
      count=count+1
      
      
j=5
if(j==5):
    print('is 5')
    
if(j==5):
    
if(j==5):
    pass

# Error unexpected EOF while parsing    
for k in range(1,3):
    
for k in range(1,3):
    pass

''' Pass statement is called dummy statement
   Pass => next normal execution '''
   
   age=990
   if(age<100):
       print("hello")
   elif (age>100):
       print('no')
   
age=990
if(age<100):
      print("hello")
elif (age>100):
       pass
   
    
print("Loop ends here")
for a in range(10):
    for b in range(20):
        if(a>=b):
            #Break the inner Loop...
            print('a>b')
            break
        else:
        #continue if the inner loop wasn't broken
           continue
    #inner loop was broken break the outer
    break


######## Key Board Input ######


str1=input("Enter your input")
str2=input("Enter your input")
print("Received input is :",str1,str2)

for i in range(5):
    a=input("Enter your input")
    print(list(a))
    
    
name=input("Enter your name")
age=input("Enter your input")
print("Welcome",name)
print("Your age is",age)
print("After 5 years, Your age will be :",(int(age)+5))
    
   
    