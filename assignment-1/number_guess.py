import random

def random_guesser(user_guess):
    score = 0
    user_guess =  int(user_guess)
    number = random.randint(1,1000)
    if user_guess == number:
        score += 1
        print("correct")
    elif user_guess > number:
        print("You were above the number! ")
    elif user_guess < number:
        print("You were below the number! ")
    elif user_guess < 0:
        print("Input a number above 0")      
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
