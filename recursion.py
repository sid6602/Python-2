# Recursion and iteration

# n!= n* n-1 * n-2 * n-3 *.....1       <-iteration
# n!= n * (n-1)!                       <-recursion

def fun_iterative(n):
    fact=1
    for i in range(n):
        fact= fact* (i+1)
    return fact


def fun_recursive(n):
    if(n==1):
        return 1
    else:
        return n* fun_recursive(n-1)
    
    
num= int(input("Enter Number:"))
print("Iterative output: ", fun_iterative(num))
print("Recursive outputL ", fun_recursive(num))
