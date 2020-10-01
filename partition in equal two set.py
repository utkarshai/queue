# Dynamic Programming based python 
# program to partition problem 

# Returns true if arr[] can be 
# partitioned in two subsets of 
# equal sum, otherwise false 
def findPartition(arr, n): 
	sum = 0
	i, j = 0, 0
	
	# calculate sum of all elements 
	for i in range(n): 
		sum += arr[i] 
	
	if sum % 2 != 0: 
		return False 
	
	part = [[ True for i in range(n + 1)] 
				for j in range(sum // 2 + 1)] 
	
	# initialize top row as true 
	for i in range(0, n + 1): 
		part[0][i] = True
		
	# initialize leftmost column, 
	# except part[0][0], as 0 
	for i in range(1, sum // 2 + 1): 
		part[i][0] = False
	
	# fill the partition table in 
	# bottom up manner 
	for i in range(1, sum // 2 + 1): 
		
		for j in range(1, n + 1): 
			part[i][j] = part[i][j - 1] 
			
			if i >= arr[j - 1]: 
				part[i][j] = (part[i][j] or
							part[i - arr[j - 1]][j - 1]) 
		
	return part[sum//2][n] 
	
# Driver Code 
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    


    if findPartition(l, n) == True: 
    	print("YES") 
    else: 
    	print("NO")

# This code is contributed 
# by mohit kumar 29 
