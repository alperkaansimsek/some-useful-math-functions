###################### Prime Number Checker ##############################
def isPrime(number):
    global isPrime
    isPrime = True
    for i in range(2, number):
        if(number % i == 0):
            isPrime = False
            break
    return isPrime
'''
#Use here if you need it. 
if(isPrime == True):
    print("number is prime")
else:
    print("number is not prime")
'''
###################### Prime Number Checker ##############################

###################### Collatz Number ##############################
def collatz(number):
    counter = 1 #This variable counts how many steps are needed to reach 1
    while (number != 1):
        if(number % 2 == 0):
            number = number / 2
        else:
            number = number * 3 + 1
        counter += 1
    return number

'''
#Use here if you need it. 
startNum = int(input())
isCollatz = collatz(startNum)
if (isCollatz == 1):
    print("this number is a collatz number.")
else:
    print("this number is not a collatz number.")
'''
###################### Collatz Number ##############################
