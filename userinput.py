# validate user input 

# check if the number specified by the user is 7 

number = input("Enter a magic number b/w 1 to 10 to proceed: ")
number = int(number)
if number == 7:
	print("You entered the right magic number!!")
else:
	print("Sorry, you failed to enter the right magic number")

