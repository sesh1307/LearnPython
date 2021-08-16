# print unlucky if num is 13 or 4
# else print odd or even
# for first 20 numbers ie 1-20

for i in range(1, 21):
	if i == 4 or i == 13:
		print(f"{i} is Unlucky!!!")
	else:
		if i % 2 == 0:
			print(f"{i} is Even!!!")
		else:
			print(f"{i} is Odd!!!") 