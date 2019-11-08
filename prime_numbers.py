
# Approach 1:
num = 18
isPrime = True
for i in [2,num-1]:
    if num % i == 0:
        isPrime = False
        break
if(isPrime):
    print (" Is a prime")
else:
    print("Not a prime")

# Approach 2
num = 29
isPrime = True
for i in [2,(num-1)/2]:
    if num % i == 0:
        isPrime = False
        break
if(isPrime):
    print (" Is a prime")
else:
    print("Not a prime")


# Approach 3
import math
num = 2
isPrime = True
for i in [2,math.sqrt(num-1)]:
    if num % i == 0:
        isPrime = False
        break
if(isPrime or num ==2 ):
    print (" Is a prime")
else:
    print("Not a prime")





