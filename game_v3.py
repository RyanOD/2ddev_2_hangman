# In our second version of Hangman, we'll limit the total number of guesses to 6 (the number of parts in our hangman)

import os	#import os class to allow for clearing of terminal screen
import random
import re

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

def get_guess():
	while True:
		guess = input("What letter do you guess? ")
		if(len(guess) > 1):
			print("Please enter a single letter only.")
		elif(not re.search('[a-zA-Z]',guess)):
			print("Only letters, please.")
		else:
			return guess 

guess = get_guess();
print(guess)