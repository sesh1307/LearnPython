'''
...Rock...
......Paper......
.........Scissors.........
'''


from random import choice

rps_list = ['Rock', 'Paper', 'Scissors']

computer1 = choice(rps_list)
computer2 = choice(rps_list)

print(computer1, computer2)

if computer1 == 'Rock':
	if computer2 == 'Rock':
		print("Both played Rock!!!!")
	elif computer2 == 'Paper':
		print("Paper beats Rock - Computer2 wins!!")
	else:
		print("Rock beats Scissors - Computer1 wins")
elif computer1 == 'Paper':
	if computer2 == 'Rock':
		print("Paper beats Rock - Computer1 wins!!")
	elif computer2 == 'Paper':
		print("Both played Paper!!!!")
	else:
		print("Scissors beats Paper - Computer2 wins")
else:
	if computer2 == 'Rock':
		print("Rock beats Scissors- Computer2 wins!!")
	elif computer2 == 'Paper':
		print("Scissors beats Paper - Computer1 wins")
	else:
		print("Both played Scissors!!!!")	