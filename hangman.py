import random

def ranword():
	f=open("wordsEn.txt") 
	word_list = f.readlines()
	f.close()
	return random.choice(word_list).strip().lower()


word = ranword()

guessed = []

guess_word = []

def drawing(n):
	if n == 0:
		print """
   ----
   |   
   |
   |
_______

"""
	if n == 1:
	  	print"""
   ----
   |  O 
   |
   |
_______

"""
	if n == 2:
		print"""
   ----
   |  O 
   |  |
   |
_______
	
"""
	if n ==3:
		print"""
   ----
   | \O 
   |  |
   |
_______"""

	if n == 4:
		print"""
   ----
   | \O/ 
   |  |
   |
_______"""

	if n == 5:
		print """
   ----
   | \O/ 
   |  |
   | /
_______"""
	if n == 6: 
		print"""
   ----
   | \O/ 
   |  |
   | / \\
_______      YOU LOSE, the word was: """ + word


for l in word:
	guess_word.append("_")

def gettit(): 	
	result = raw_input("Guess a letter, bitch: ").lower()
	if len(result) == 1:
		return result[0]
	else:
		return gettit()

drawing(0)
print " ".join(guess_word)

while len(guessed)<6 and "_" in guess_word:
	guess = gettit()
	for i in range(len(word)):
		if word[i] == guess:
			guess_word[i]=word[i] 
	if not guess in word:
		guessed.append(guess)
	
	drawing(len(guessed))
	
	print "Not in word, loser: "+ " ".join(guessed) 

	print " ".join(guess_word) 
	
if not "_" in guess_word:
	print "You Win!!! Now go back to your bleak, pathetic life..."

