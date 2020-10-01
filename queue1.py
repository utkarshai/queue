# Python3 program to reverse a queue 
from queue import Queue 

# Utility function to print the queue 
def Print(queue): 
	while (not queue.empty()): 
		print(queue.get(), end = ", ") 
		# queue.get() 

# Function to reverse the queue 
def reversequeue(queue): 
	Stack = [] 
	while (not queue.empty()): 
		Stack.append(queue.queue[0]) 
		queue.get() 
	while (len(Stack) != 0): 
		queue.put(Stack[-1]) 
		Stack.pop() 



# Driver code 
if __name__ == '__main__': 
  queue = Queue() 
  queue.put(10) 
  queue.put(20) 
  queue.put(30) 
  queue.put(40) 
  queue.put(50) 
  queue.put(60) 
  queue.put(70) 
  queue.put(80) 
  queue.put(90) 
  queue.put(100) 
  
  a=queue.qsize()
  for i in range(a):
    print(queue.queue[i], end=", ")
  for i in range(a-1, -1, -1):
    print(queue.queue[i], end=", ")
    
  reversequeue(queue) 
  Print(queue) 

# This code is contributed by PranchalK 
