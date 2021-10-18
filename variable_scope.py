#Local and Global Scope

l= 10      #Global scope
def fun_1():
    l=5    #local scope
    print("In Local scope of function: ", l)
    
fun_1()
print("In global scope: ",l)
