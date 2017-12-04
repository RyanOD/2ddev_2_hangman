# In our first version of this game, we'll allow players to have unlimited guesses. This will allow us to simplify the game
# and build it incrementally rather than tackling the entire game on the first pass.

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

words = ["apron","alien","bacon","blade","cabin","curve","drone","ditch","elbow","epoxy","fancy","flyer","gecko","ghost","horse",
		 "human","jumbo","junky","klutz","knife","mango","mouse"]

#words = ["time","year","people","thing","woman","life","child","world","school","state","family","student","group","country",
#		"problem","hand","part","place","case","week"]

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

print(words[word_num])

# total number of hits cannot be 
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


# how to set up the control flow of the game? at first glance, you might consider any of the following...
# track hits, track misses, track number of guesses, etc.
# its true there are a number of variables to track in this game: hits/misses, number of guesses, max guesses,
# the word, the letters that have been guessed, etc.

#get letter
#check each position in word arrray for match
#if match, copy letter into empty array
#increment hit for each match
#if hit == length of word, winner!
