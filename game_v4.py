# In the third version of our hangman game, we allow for words with repeated letters. We accomplish this by
# introducing a new variable, "hidden_hit", that tracks the number of actual alpha characters we have successfully
# filled in

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

words = ["apron","alien","bacon","blade","cabin","curve","drone","ditch","elbow","epoxy","fancy","flyer","gecko","ghost","horse",
		 "human","jumbo","junky","klutz","knife","mango","mouse"]

hang_state = [
	"\t ______\n\t |   |\n\t |\n\t |\n\t |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |\n\t |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |   |\n\t |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |  /|\n\t |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |  /|\\\n\t |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |  /|\\\n\t |   |\n\t |\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |  /|\\\n\t |   |\n\t |  /\n\t |\n\toooo",
	"\t ______\n\t |   |\n\t |   O\n\t |  /|\\\n\t |   |\n\t |  / \\\n\t |\n\toooo"
]

print("Welcome to Hangman!")

hit = 0
hidden_hit = 0
miss = 0

word = list(words[random.randint(0,len(words) - 1)])		# list function converts string into array by character
word_build = []
guess_tracker = []

def get_guess():
	while True:
		guess = input("What letter do you guess? ")
		if(len(guess) > 1):
			print("Please enter a single letter only.")
		elif(not re.search('[a-zA-Z]',guess)):
			print("Only letters, please.")
		else:
			return guess

for x in range(0,len(word)):
	word_build.append("_")

while (hidden_hit < len(word)):
	guess = get_guess()








	if guess in guess_tracker:
		print("You already guessed that letter. Please try again.")
		continue	# forgoes the remainder of the while loop

	elif guess in word:
		guess_tracker.append(guess)
		for x in range(0,len(word)):
			if(word[x] == guess):
				word_build[x] = guess
				hidden_hit += 1
		hit += 1

	else:
		guess_tracker.append(guess)
		miss += 1

	for x in word_build:
		print(x,end='')
	print("     Hit = " + str(hit) + "    Miss = " + str(miss) + "\n")

print("Congratulations! You win!")