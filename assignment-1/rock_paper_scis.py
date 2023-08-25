import random

user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]

while True:
    user_pick = input("enter r for rock, p for paper and s for scissor or Q to exit ").lower()
    if user_pick == "q":
        break

    if user_pick not in options:
        continue
    
    sel = random.randint(0,2)

    computer_pick = options[sel]
    if user_pick == "r" and computer_pick == "s":
        print("You Won ")
        user_wins += 1
    elif user_pick == "s" and computer_pick == "p" :
        print("You Won ")
        user_wins += 1
    elif user_pick == "p" and computer_pick == "rock":
        print("You Won ")
        user_wins += 1       
    elif user_pick == computer_pick:
        print("TIE")
    else:
        print("You Lose ")
        computer_wins += 1

print("user score",user_wins)        
print("computer score", computer_wins)
        