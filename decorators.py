print("Code 1")
def fun1():
    print("hey")

fun2= fun1
fun2()


print("\n\nCode 2")

def fun(num):
    if num==0:
        return print
    if num==1:
        return int
a=fun(1)
print(a)


print("\n\nCode 3")
def exec(fun1):
    fun1("This")
exec(print)


print("\n\nCode 4")
def dec1(func1):
    def now():
        print("Before fun: ")
        func1()
        print("After fun")
    return now()

@dec1
def fun2():
    print("Hey it's a execution")



