import math

def check_prime(n):
    sq=math.sqrt(n)
    for i in range(2,int(sq)+1):
        if n%i==0:
            return False
            
    return True

def printing(n):
    for i in range(1,n+1):
        if check_prime(i):
            print(i)
        else:
            continue

print("CHECKING PRIME NUMBERS")
number=int(input("Enter the number: "))
if check_prime(number):
    print(number," is a prime number")
else:
    print(number," is not a prime number")
print("\n Prime numbers upto ",number," are:")
printing(number)
