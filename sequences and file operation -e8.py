#if else statement

a=15
b=10
if(a==25):
    print("a is 25")
    if(b==10):
        print("b is equal to 10")
        print("End")
        
elif(10<=a<=25):
    print("In between 10and 25")
    if(b==10):
        print("b is equal to 10")
        print("End")

else:
    print("Greater than 25")
    
    
    
    ################## File Handling ###################
    
       
newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","w")

newfile.write("Hello, Welcome to Python write some text using w mode")
newfile.write("\n Hello, welcome to Python")


newfile.close()




newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","w")

newfile.write("Hello, Welcome to Python write some text using w mode")
newfile.write("\n Hello, welcome to Python")

for i in range(1,10):
    newfile.write("\n Hello, welcome to Python")
    
newfile.close()


### reading file

newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","r")    #default is "r mode"

newfile.readline()

for i in range(0,20):
    print(newfile.readline())
    
newfile.readline()

print(newfile.tell())    #current cursor position

newfile.seek(0)


newfile.seek(0)
filedata=newfile.readlines()   #reads the entire lines and store in a variable


filedataread=newfile.read()   #entire file will be loaded as string object or text form


newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","a")  # append mode existing file in append mode




newfile=open("C:\\Users\\hp\\Desktop\\files\\tr1.txt","a")  #it will try to create a new file

newfile.write("Hello, Welcome to Python write some text using w mode")

newfile.close()



newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","a")  # append mode existing file in append mode

newfile.write("\n Hello, Welcome to Python using a mode")
newfile.close()


print(newfile.tell())
newfile.seek(0)


for i in range(1,10):
    newfile.write("\nHello a mode")
    
newfile.close()


# w+ mode write and read mode

#normal write 

newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","w")

newfile.write("Hello, Welcome to Python write some text using w mode")
newfile.write("\n Hello, welcome to Python")


newfile.close()
    

#Exclusive mode

newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","w+")

newfile.write("Hello, Welcome to Python write some text using w mode")
newfile.write("\n Hello, welcome to Python")

newfile.readline()
print(newfile.tell())
newfile.seek(0)


newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","a+")

newfile.write("Hello, Welcome to Python write some text using a mode")
newfile.write("\n Hello, welcome to Python")

newfile.readline()
print(newfile.tell())
newfile.seek(0)
newfile.close()

#r+ mode

newfile=open("C:\\Users\\hp\\Desktop\\files\\tr.txt","r+")
newfile.readline()
print(newfile.tell())
newfile.seek(0)

newfile.write("\n Hello, welcome to Python write some text using r+ mode")

for i in range(0,20):
    #print(newfile.readline())
    pass

filedata=newfile.readlines()
filedataread=newfile.read()
newfile.write("Hello, Welcome to Python write some text using a mode")





newfile.close()


    

