# Name
# Rock Paper Scissors
# added comment
# VARIABLES
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r" , "p" , "s"]


# Welcome Message
# Print the Message
print("welcome to Rock Paper Scissors")
# prompt for player name
pName = input("What is your name? ")

# Game Loop

# Final Score
def printScore():
	# Write message	
	print("The score is: ")
	# Write player score	
	print(pName + ": " + str(pScore))
	# Write computer score	
	print("Computer: " + str(cScore))
	# Write how many ties	
	print("Ties: " + str(ties))

# Game loop
# make a forever loop
while True:
	# Print current score
	printScore()
	# prompt for a choice (r (rock), p (paper), s (scissors), q (quit)
	pChoice = input("Enter r (rock), p (paper), s (scissors), q (to quit): ")
	# deal with player entering q
	if pChoice == "q":
		print(pName + " has quit the match")
		break
	# get computers choice(random)
	cChoice = random.choice(computerChoices)
	# compare for player entering r
	if pChoice == "r":
		print(pName + " picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("Paper covers Rock")
			cScore = cScore + 1
		# if computer is s
		else:
			print("Computer picked Scissors")
			print("Rock breaks Scissors")
			pScore = pScore + 1

	# compare for player entering p
	elif pChoice == "p":
		print(pName + " picked Paper")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Paper covers Rock")
			pScore = pScore + 1
		elif cChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer picked Scissors")
			print("Scissors cuts Paper")
			cScore = cScore + 1
		pass
	# compare for player entering s
	elif pChoice == "s":
		print(pName + " picked Scissors")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Rock breaks Scissors")
			cScore = cScore + 1
		elif cChoice == "p":
			print("Computer picked Paper")
			print("Scissors cuts Paper")
			pScore = pScore + 1
		else:
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
		pass
	# deal with player entering anything else




