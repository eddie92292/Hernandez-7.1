# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Edward Hernandez
# Creation Date: Dec 5, 2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    #print('''You are in a land full of dragons. In front of you,
    #you see two caves. In one cave, the dragon is friendly
    #and will share his treasure with you. The other dragon
    #is greedy and hungry, and will eat you on sight.''')
        print('You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
        #Correction 1: Too many quotations
        #Correction 2: Return spaces caused the print statement to be broken
#print()
#Correction 3: change print to displayIntro()
displayIntro()

def chooseCave():
    cave = ''
    #while cave != '1' and cave != '2':
        #print('Which cave will you go into? (1 or 2)')
        #cave = input()
        #Correction 4: too many indents
    while cave != '1' and cave != '2':
            print('Which cave will you go into? (1 or 2)')
            cave = input()
    #Correction 5: caves changed to cave, caves not defined
    #return caves
    return cave
#Correction 6: chooseCave defined and implimented
chooseCave()
def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #print 'Gobbles you down in one bite!'
                #Correction 7 Parenthesis needed
                print ('Gobbles you down in one bite!')

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
#Correction 8 needs ==
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    #caveNumber = choosecave()
    #Correction 9: choosecave() changed to chooseCave()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        #print("Thanks for planing")
        #Correction 10: change planing to playing
        print("Thanks for playing")

