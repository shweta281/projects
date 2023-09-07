import random
x=random.randint(0,11)
print("guess the number between one to ten (you get a total of 3 chances):- ")
count=0
while count<3:
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ",count, " try")
		break
	elif x>guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
if count>3:
	print("the number was:",x)
	print("Better Luck Next time!")
