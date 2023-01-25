###################### Prime Number Checker ##############################
def isPrime(number):
    global isPrime
    isPrime = True
    for i in range(2, number):
        if(number % i == 0):
            isPrime = False
            break

if(isPrime == True):
    print("number is prime")
else:
    print("number is not prime")
###################### Prime Number Checker ##############################
