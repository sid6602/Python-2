# Global variable in nexted function

x=100
def fun1():
    x=10
    def fun2():
        global x
        x=88
    print("Before calling fu2", x)
    fun2()
    print("After calling fun2", x)
    
fun1()
print("Printing global scope:" , x)
