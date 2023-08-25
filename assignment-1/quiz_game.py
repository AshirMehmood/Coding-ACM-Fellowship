print("Welcome to my quiz")

playing = input("Do you want to play? ") 

    
if playing.lower() == "yes":
    score = 0
    print("Okay, lets play ; )") 

    answer = input("what does CPU stand for? ")   

    if answer.lower() != "central processing unit":
         print("oh snap, not correct")
    else:
        print("correct")
        score += 1    

    answer = input("what does gpu stand for?")

    if answer.lower() != "graphics processing unit":
        print("oh snap, not correct")
    else:
        print("correct")
        score += 1    

    answer = input("what does psu stand for?")
    if answer.lower() != "power supply unit":
        print("oh snap, not correct")
    else:
        print("correct")
        score += 1 

    score = str(score)
    print("your score is " + score)    
    quit()


if playing != "yes" or "YES":
    quit()    