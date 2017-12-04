# In the second version of our hangman game, we will deal with ability to guess the same letter multiple times and
# introduce words with repeating letters

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
miss = 0

word = list(words[random.randint(0,len(words) - 1)])		# list function converts string into array by character
word_build = []
guess_tracker = []

for x in range(0,len(word)):
	word_build.append("_")

while (hit < len(word)):
	guess = input("What letter do you guess? ")

	if guess in guess_tracker:
		print("You already guessed that letter. Please try again.")
		continue

	elif guess in word:
		guess_tracker.append(guess)
		word_build[word.index(guess)] = guess
		hit += 1

	else:
		guess_tracker.append(guess)
		miss += 1

	for x in word_build:
		print(x,end='')
	print("     Hit = " + str(hit) + "    Miss = " + str(miss) + "\n")

print("Congratulations! You win!")