def IsPrime( Number ):
	divisor = 3
   	while divisor <= Number/2:
   		if Number % divisor == 0:
   			return False
   		divisor = divisor + 1
   	return True

NumberPrimes = 3
MaxPrimes = 100
CurrentNumber = 3
print "(1): 1"
print "(2): 2"
while NumberPrimes <= MaxPrimes:
	if IsPrime(CurrentNumber):
		print "(", NumberPrimes, "): ", CurrentNumber
		NumberPrimes = NumberPrimes + 1
	CurrentNumber = CurrentNumber + 2

