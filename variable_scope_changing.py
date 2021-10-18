#Local and Global Scope

l= 10      #Global scope
def fun_1():
    global l
    l =l+50
    print("In Local scope of function: ", l)
    
fun_1()
print("In global scope: ",l)
print("Changes original global vaiable")
