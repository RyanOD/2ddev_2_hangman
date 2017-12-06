# In our first version of this game, we'll allow players to have unlimited guesses. This will allow us to simplify the game
# and build it incrementally rather than tackling the entire game on the first pass. There will also be no error handling.

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

guess_limit = 6
word_num = random.randint(0,len(words) - 1)
word = list(words[word_num])
word_build = []
for x in range(0,len(word)):
	word_build.append("_")

hit = 0
miss = 0

while (hit < len(word)):
	guess_state = 'miss'
	guess = input("What letter do you guess? ")
	for x in range(0,len(word)):
		if(guess == word[x]):
			guess_state = 'hit'
			word_build[x] = word[x]
			hit += 1

	if(guess_state == 'miss'):
		miss += 1

	print("\n  ",end='')
	for x in range(0,len(word_build)):
		print(word_build[x],end='')
	print("\n")
	print("  Hit = " + str(hit) + "    Miss = " + str(miss) + "\n")


print("Congratulations! You win!")
