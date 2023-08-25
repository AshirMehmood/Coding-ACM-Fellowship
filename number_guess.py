import random

def random_guesser(user_guess):
    score = 0
    number = random.randint(0,1000)
    if user_guess == number:
        score += 1
        print("correct")
    else:
         score -= 1
         print("not correct") 
    print(number)
    print("your score: ",score)       



play = True

while play == True:
    
    user_guess = input("enter the number between 1-1000! ")
    random_guesser(user_guess)    
    cont = input("do you want to play guess game again? press 1 to play | press any key to exit --")
    if cont != 1:
        play = False    
