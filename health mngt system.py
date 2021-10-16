# Health management System
def getdate():
    import datetime
    return datetime.datetime.now()

def retrive(a):
    try:
        if(a==1):
            f=open("sid_food1.txt")
            content1=f.read()
            print(content1)
            f1=open("sid_exercise1.txt")
            content2=f1.read()
            print(content2)

        elif(a==2):
            f2=open("ishu_food.txt")
            content3=f2.read()
            print(content3)
            f3=open("ishu_exercise.txt")
            content4=f3.read()
            print(content4)

        elif(a==3):
            f4=open("omi_food.txt")
            content5=f4.read()
            print(content5)
            f5=open("omi_exercise.txt")
            content6=f5.read()
            print(content6)
        else:
            print("In valid choise")
    except Exception as e:
        print(e, "\n No data entered to show you")
        
def add_exe(b):
    date=str(getdate())
    if(b==1):
        f1=open("sid_exercise1.txt", "a")
        f1.write("[ ")
        f1.write(date)
        f1.write("]   ")
        f1.write(input("Exercise of sid?"))
        f1.write("\n")
        
    elif(b==2):
        f3=open("ishu_exercise.txt", "a")
        f3.write("[ ")
        f3.write(date)
        f3.write("]   ")
        f3.write( input("Exercise of ishu?"))
        f3.write("\n")
    
    elif(b==3):
        f5=open("omi_exercise.txt", "a")
        f5.write("[ ")
        f5.write(date)
        f5.write("]   ")
        f5.write( input("Exercise of omi?"))
        f5.write("\n")
        
    else:
        print("In valid choise")
    
    
    
def add_food(c):
    date=str(getdate())
    if(c==1):
        f=open("sid_food1.txt", "a")
        f.write("[ ")
        f.write(date)
        f.write("]   ")
        f.write( input("Food of sid?"))
        f.write("\n")
    
    elif(c==2):
        f2=open("ishu_food.txt", "a")
        f2.write("[ ")
        f2.write(date)
        f2.write("]   ")
        f2.write( input("Food of ishu?"))
        f2.write("\n")
    
    elif(c==3):
        f4=open("omi_food.txt", "a")
        f4.write("[ ")
        f4.write(date)
        f4.write("]   ")
        f4.write(  input("Food of omi?"))
        f4.write("\n")
    else:
        print("In valid choise")
    
    
sett=1    
while(sett==1):    
    print("Enter \n 1 to retrive \n 2 to add log \n")
    num1=int(input())
    if(num1==1):
        print("\n\nEnter \n 1 for sid \n 2 for ishu \n 3 for omi \n")
        num2=int(input())
        retrive(num2)

    if(num1==2):
        print("\n\nEnter \n 1 for adding exercise \n 2 for adding food\n\n")
        num3=int(input())

        if(num3==1):
            print("\n\nEnter \n 1 for sid \n 2 for ishu \n 3 for omi\n")
            num4=int(input())
            add_exe(num4)
        elif(num3==2):
            print("\n\nEnter \n 1 for sid \n 2 for ishu \n 3 for omi\n")
            num5=int(input())
            add_food(num5)
        else:
            print("Invalid")


    print("\n\n y - more operations \n n- terminate")
    last=str(input())
    if(last== "y"):
        sett=1
        print("\n\n")
    elif(last=="n"):
        sett=0
