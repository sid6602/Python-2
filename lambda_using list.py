# lambda using list

def sorting(a):
    return a[0]

a= [[10,4], [4,6], [56,1]]
a.sort(key=sorting)
print(a)

# using lambda

b=[[2,3], [45,7],[3,5]]
b.sort(key=lambda x:x[1])
print(b)
