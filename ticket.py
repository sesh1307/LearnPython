# ticketing system
'''
< 10 yrs - child fee - Rs.5
>10 < 18 - young adult fee - Rs. 10
>=18 - adult fee - Rs.15

'''

age = input("Enter your age: ")

if age:
	age = int(age)
	if age >= 18:
		print("you are an adult and you pay Rs.15")
	else:
		if age < 10:
			print("You are a child and you pay Rs.5")
		else:
			print("You are an young adult and you page Rs.10")
else:
	print("You didnt enter a age")