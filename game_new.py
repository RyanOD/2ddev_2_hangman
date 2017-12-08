# In the second version of our hangman game, we track which letters have been guessed and ask the player to guess a new
# letter if they mistakenly choose the same letter more than once. The second version of this game is a major refactoring of the first.

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

words = ["appprooon"]

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

prohibited_list = ['','1','2','3','4','5','6','7','8','9','0']

print("Welcome to Hangman!")

hit = 0
miss = 0

word = list(words[random.randint(0,len(words) - 1)])		# list function converts string into array by character
word_build = []
guess_tracker = []

for x in range(0,len(word)):
	word_build.append("_")

while (alive == True):
	guess = input("What letter do you guess? ")

	if guess in prohibited_list:
		print("Please input letters only...")
		continue

	if guess in guess_tracker:
		print("You already guessed that letter. Please try again.")
		continue

	guess_tracker.append(guess)

	if guess in word:
		for x in range(0,len(word)):
			if(word[x] == guess):
				word_build[x] = guess
	else:
		miss += 1

	print(hang_state[miss],end="\n\n\t")
	
	for x in word_build:
		print(x,end='')
	print("\n")