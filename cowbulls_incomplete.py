import random

def compare_numbers(number, user_guess):
    #intializing the variable cow and bull in order to count 
    cow=0
    bull=0
    for i in range(len(number)):
        if user_guess == number:
                bull +=1
        elif user_guess in number:
                cow +=1 
    return (cow,bull)

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number)# adding apporiate brackets 

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!: ") #changed raw_input to input
    if user_guess == "exit":
        print("have a nice day! goodbye") 
        break


    cowbullcount = compare_numbers(number,user_guess)
    if cowbullcount == (0,0):
            continue

    guesses +=1     

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
 
else:
        print("Your guess isn't quite right, try again.")
