# Python 3 program to generate well 
# ordered numbers with k digits. 

# number --> Current value of number. 
# x --> Current digit to be considered 
# k --> Remaining number of digits 
def printWellOrdered(number, x, k): 

	if (k == 0): 
		print(number, end = " ") 
		return

	# Try all possible greater digits 
	for i in range( (x + 1), 10): 
		printWellOrdered(number * 10 + i, 
								i, k - 1) 

# Generates all well ordered 
# numbers of length k. 
def generateWellOrdered(k): 
	printWellOrdered(0, 0, k) 

# Driver code 
if __name__ == "__main__": 
	
	k = 3
	generateWellOrdered(k) 

# This code is contributed by Ita_c 
