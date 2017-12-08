# In the first version of our hangman game, we track which letters have been guessed and ask the player to guess a new
# letter if they mistakenly choose the same letter more than once. We use no functions which leads to some verbose code.

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

# variables to track letters hits and misses
hit = 0
miss = 0

# variable to store secret word selected at random from words array
word = words[random.randint(0,len(words) - 1)]

# convert word string into a list array
word_list = list(word)

# unique letter count in secret word
unique_letters = len(set(word))

# arrays to track correct guesses and all guesses
guesses_correct = []
guesses_all = []

# set up array to track correct guesses
for x in range(0,len(word)):
	guesses_correct.append("_")

# print initial game state to establish hangman gallows and number of unknown letters
print(hang_state[0],end="\n\n\t")
for x in guesses_correct:
	print(x,end='')
print('\n\n')

# game play loop runs as long as misses is less than length of the hang_state list (minus the inital state) or total hits is less than unique letters in secret word
while(miss < len(hang_state)-1 and hit < unique_letters):
	guess = input("Please guess a letter: ")

	if guess in guesses_all:
		print("You already guessed that letter. Please try again.")
		continue

	guesses_all.append(guess)

	# check to see if guess is in secret word, if so, add word to correct guesses list and increment hit variable. if not, increment miss variable.
	if guess in word_list:
		for x in range(0,len(word_list)):
			if(word_list[x] == guess):
				guesses_correct[x] = guess
		hit += 1
	else:
		miss += 1

	# clear screen and print currect game state (gallows)
	os.system('clear')
	print(hang_state[miss],end="\n\n\t")
	
	# print current game state (secret word and total guess list)
	for x in guesses_correct:
		print(x,end='')
	print("\t\t\tGuess Letters: ",end='')
	for x in guesses_all:
		print(x,end='')
	print("\n")

# game play loop has ended. check to see if player has won or lost based on miss total
if(miss >= len(hang_state)-1):
	print("You lose. Please try again.")
else:
	print("You win! The secret word was " + word + '.')