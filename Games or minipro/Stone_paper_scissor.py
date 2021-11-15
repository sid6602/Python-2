import random

user_count=0
comp_count=0
chance=1

print("You have 10 chances")

while chance<=10:
    
    print("\n\n\nChances: ", chance)
    
    a=str(input("Select your choice: Stone, Paper, Scissor"))
    if(a=="Stone" or a=="Paper" or a=="Scissor"):
       
        List1= ["Stone", "Paper", "Scissor"]
        comp=random.choice(List1)
        print("\nComp: ", comp)
        print("You: ", a)

        if(a == comp):
            print("Match Dwaw!!")

        elif(a=="Stone" and comp=="Scissor"):
            print("You Win chance", chance, "!!!")
            user_count=user_count+1

        elif(a=="Paper" and comp=="Stone"):
            print("You Win chance", chance, "!!!")
            user_count=user_count+1

        elif(a=="Scissor" and comp=="Paper"):
            print("You Win chance", chance, "!!!")
            user_count=user_count+1

        elif(a=="Stone" and comp=="Paper"):
            print("You Lost chance", chance, "!!!")
            comp_count=comp_count+1

        elif(a=="Paper" and comp=="Scissor"):
            print("You Lost chance", chance, "!!!")
            comp_count=comp_count+1

        elif(a=="Scissor" and comp=="Stone"):
            print("You Lost chance", chance, "!!!")
            comp_count=comp_count+1

        chance=chance+1
    
     
    else:   
        print("Invalid Choise")
if(chance>=10):
    print("\n\nGame Over")
if(user_count > comp_count):
    print("You Win the game")
elif(user_count < comp_count):
    print("You lost to the comp")
