#Time Module

import time

initial= time.time()


k=0
while(k<10):
    print("Siddhi")
    time.sleep(1)
    k+=1
print("While loop timing: ", time.time() - initial, "\n")

initial2= time.time()    
for i in range(10):
    print("siddhi")
    
print("For loop timing: ", time.time() - initial2, "\n\n")

print("Current time")

print(time.asctime(time.localtime(time.time())))
