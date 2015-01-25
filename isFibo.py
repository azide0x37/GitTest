import math

def isFibo(test):
	if math.sqrt(5*test**2 - 4).is_integer() or math.sqrt(5*test**2 + 4).is_integer():
		return True
	else:
		return False

def seqFibo(fibo):
	fiboLast = 0
	for n in range(1,fibo):
		if isFibo(fibo - n):
			fiboLast = fibo-n
			return fibo + fiboLast
def nextFibo(test):
	counter = test
	while counter > 0:
		if isFibo(counter):
			return counter
		counter -= 1

def prevFibo(test):
	counter = 0
	while counter >= (test):
		if isFibo(counter):
			return counter
		counter += 1
		
while not str(raw_input("Press 'n' to exit.")):
	try:
		print 
		test = int(raw_input('Enter a number to find the next Fibonacci number '))
		if type(test) == int: 
			if isFibo(test):
				print test, "is in the fibonacci sequence, and", seqFibo(test), "is it's successor!"
			else:
				print test, "is not a fibonacci number", nextFibo(test), "is the highest Fibonacci number less than",test
		else:
			print test, "Is not a number"
	except:
		print "Invalid entry, try again with a number!"
