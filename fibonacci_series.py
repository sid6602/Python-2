# fibonacci series

def fibb(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fibb(n-1) +fibb(n-2)
    
    
num= int(input("Enter Number:"))
print("Iterative output: ", fibb(num))
