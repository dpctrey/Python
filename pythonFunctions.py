# Making functions
# Checking primes
# Using print format

def addNum(n, m):
    sum = 0
    sum = n + m
    return sum
    
def subNum(n, m):
    dif = 0
    dif = n - m
    return dif

def isPrime(n):
    if n == 1:
        answer = "1 is a special case!"
        return answer
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            answer = "The number is not prime!"
            return answer
    else:
        print(n, "is a prime number")
        answer = "The number is prom!"
        return True

addNum(2,3)
subNum(10,4)
for n in range(1,25):
    myAnswer = isPrime(n)