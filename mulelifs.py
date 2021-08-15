# simple program to demonstrate multiple elif

color = input("Select any one of the allowed colors red / blue / black / grey / yellow / white : ")
color = color.lower()

if color == 'red':
	print("Good choice, like a sunset sky!!!")
elif color == 'blue':
	print("Cool choice, like a clear sky!!!")
elif color == 'black':
	print("when in doubt go for black!!!")
elif color == 'grey':
	print("if you want something close to black")
elif color == 'yellow':
	print("Bright choice, like the glowing Sun")
elif color == 'white':
	print("you need to take extra care!!")
else:
	print("Enter a color that is allowed as of now")