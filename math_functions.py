###################### Prime Number Checker ##############################
def isPrime(number):
    prime = True
    for i in range(2, number):
        if(number % i == 0):
            prime = False
            break
    return prime

'''
# Use here if you need it.
result = isPrime(99)
print(result)
if(result == True):
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
