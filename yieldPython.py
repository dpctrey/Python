# Using yield and increment
# New way of checking true
def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
        
def checkPrimes(n = 1):
    while(True):
        if isPrime(n): yield n
        n += 1

for n in checkPrimes():
    if n < 100:
        print(n)