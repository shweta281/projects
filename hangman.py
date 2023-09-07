
import random
from collections import Counter
someWords=["cow","dog","elephant","tiger"]
word = random.choice(someWords)
print('Guess the word...')
for i in word:
	print('_', end=' ') #printing blank space for each word
print()
playing=True
letterGuessed=''   
chances=len(word)+1
correct=0
flag=0
while (chances != 0) and flag == 0: # flag is updated when the word is correctly guessed
	print()
	chances -= 1
	guess=input('Enter a letter to guess: ')
			# checking if the only a letter has been entered
	if not guess.isalpha():
		print('Enter only a LETTER')
		continue
	elif len(guess)>1:
		print('Enter only a SINGLE letter')
		continue
	elif guess in letterGuessed:
		print('You have already guessed that letter')
		continue

	if guess in word:
		# k stores the number of times the guessed letter occurs in the word
		k = word.count(guess)
		for _ in range(k):
			letterGuessed += guess # The guess letter is added as many times as it occurs

			# Print the word
	for char in word:
		if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
			print(char, end=' ')
			correct += 1
		# If user has guessed all the letters
		elif (Counter(letterGuessed) == Counter(word)):
			print()
			print(word)
			flag = 1
			print('Congratulations, You won!')
			break 
		else:
			print('_', end=' ')
if(flag!=1):
    print()
    print("you lose :(")

