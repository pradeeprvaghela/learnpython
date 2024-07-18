import random
computer = random.randint(-1, 1)
userip = input("Enter your choise : ")
con={"s":1, "w":-1, "g":0}
retcon={1:"Snake", -1:"Water", 0:"Gun"}
you = con[userip]
print(f"Computer choose : {retcon[computer]} \n You choose : {retcon[you]}")
if(computer == 1 and you == -1):
    print("computer win")
elif(computer == -1 and you == 1):
    print("you win")
elif(computer == 1 and you == 0):
    print("you win")
elif(computer == 0 and you == 1):
    print("computer win")
elif(computer == -1 and you == 0):
    print("computer win")
elif(computer == 0 and you == -1):
    print("you win")
else:
    print("It's Draw")