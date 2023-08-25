answer = input("You came across two paths, take left or right ")

if answer.lower() == "left":
    answer = input("you came across a river, do want to walk through road or swim ? ") 
    if answer.lower() == "swim":
        print("You were eaten by alligator")
        quit()
    elif answer.lower()  ==  "walk":
        print("You walked for many miles and ran out of water, You lose")
        quit()
    else:
        print("invalid, you lose!")

elif answer.lower() == "right":
    answer = input("You come across a wobbly bridge, do you want to cross or go back ? ")
    if answer.lower()  == "back":
        print("You go back and lose !")          
    elif answer.lower() == "cross":
        answer = input("You come across a stranger, who is offering gold ? ")
        if answer.lower() == "take":
            print("You win !")        
        else:
            print("invalid, you lose!")
    else:
        print("invalid, you lose!")          

else:
    print("invalid, you lose!")        