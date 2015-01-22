import math

def isFibo(test):
	if math.sqrt(5*test**2 - 4).is_integer() or math.sqrt(5*test**2 + 4).is_integer():
		return True
	else:
		return False

def nextFibo(fibo):
	fiboLast = 0
	for n in range(1,fibo):
		if isFibo(fibo - n):
			fiboLast = fibo-n
			return fibo + fiboLast

while raw_input('Continue? ') != 'N\n' or 'n\n':
	try:
		test = int(raw_input('Enter a number to find the next Fibonacci number '))
		if type(test) == int: 
			if isFibo(test):
				print test, "is in the fibonacci sequence, and", nextFibo(test), "is it's successor!"
		else:
			print test, "Is not a number"
	except:
		print "Invalid entry, try again with a number!"
