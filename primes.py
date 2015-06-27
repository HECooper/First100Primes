# So basically IsPrime is the Number(function), which shows whether a number is prime or not.

def IsPrime( Number ):
    #if even return false
    if Number % 2 == 0:
        return Number == 2
#The divisor is 3 and above to get to the prime numbers.
    divisor = 3
#If the divisor is equal to or less than the number divided by 2 it is not prime.
    while divisor <= Number/2:
        #If the number and the divisor equal 0, it is not prime.
        if Number % divisor == 0:
            return False
#if the divisor = the divisor + 1 the number is prime (CONGRATULATIONS) i lied you actually have to test th next divisor
        divisor = divisor + 1
    return True
#So the number of primes = 3, because 2 and 1 are already prime.
NumberPrimes = 3
#The Max number of primes is 100, because we only want 100 prime numbers.
MaxPrimes = 100
#The number that we are currently on is 3, because we already know 2 and 1 are prime and are special cases.
CurrentNumber = 3
#print out 2 and 1 because -ONCE AGAIN- we know they are prime
print "(1): 1"
print "(2): 2"
#While numberprimes is equal to or less than Max Primes
while NumberPrimes <= MaxPrimes:
# Is prime is equal to the current, print out NumberPrimes and CurrentNumber
    primetrueorfalse = IsPrime(CurrentNumber)
    if primetrueorfalse == True:
        print "(", NumberPrimes, "): ", CurrentNumber
#the rule for this is that numberprimes = numberprimes + 1
        NumberPrimes = NumberPrimes + 1
#and the rule for current number is that current number = currentnumber + 2 
    CurrentNumber = CurrentNumber + 2
#WE ARE DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

