from random import randint
computer = randint(1,100)
guess=1
for i in range(50):
    user=int(input("guess the number : "))
    if computer < user:
        print("Lower number please")
        guess+=1
    elif computer > user:
        print("Higher number please")
        guess+=1
    else:
        print(f"Correct at the guess number {guess}")
        break

