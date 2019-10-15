#Import required packages
import random

#Define variables needed (NOTE:inline; this section not relevant)

#User input for userChoice
while True:
    try:
        userChoice = int(inpu\t("Enter a choice (1 = Rock 2 = Paper 3 = Scissors): "))
    except ValueError:
        print("Sorry, please enter a number between 1 and 3")
        continue
    else:
        break
userChoice = userChoice - 1

#Randomize computerChoice
computerChoice = random.randrange(0,2,1)

#Compare choices to determine winner


#Show winner

#Advanced:
#   -Develop methods for random choice
#   -Develop method for determining winner
#   -Develop method for displaying winner
#   -Apply loop for continuous play
#   -Apply scoring system