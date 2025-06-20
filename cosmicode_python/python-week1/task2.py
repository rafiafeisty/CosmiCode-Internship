import math

def modulo():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1%num2
    print(num1," modulo ",num2," : ",result)
    print()
    return

def power():
    num1=int(input("Enter the base number: "))
    num2=int(input("Enter the exponent number: "))
    result=1
    for i in range(num2):
        result*=num1
    print(num1,"^",num2,": ",result)
    print()
    return

def square_root():
    num1 = float(input("Enter the number: "))
    if num1 < 0:
        print("Square root not defined for negative numbers.")
        return
    low = 0
    high = max(1, num1)
    epsilon = 1e-6
    while (high - low) > epsilon:
        mid = (low + high) / 2
        if mid * mid > num1:
            high = mid
        else:
            low = mid
    print("Approximate square root is:", round(mid, 6))
    print()
    return

def percentage():
    num1 = float(input("Enter the percentage: "))
    num2 = float(input("Enter the number: "))
    result=(num1/100)*num2
    print(num1,"percent of",num2,": ",round(result,5))
    print()
    return

def logarithmic():
    num1 = float(input("Enter the number: "))
    base = float(input("Enter the base: "))
    result=math.log(num1,base)
    print("Logarithm of",num1,"with base",base,": ",result)
    print()
    return

def main():
    while(True):
        print("1- Modulo")
        print("2- Power")
        print("3- Square Root")
        print("4- Percentage")
        print("5- Logarithmic")
        print("6- Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            modulo()
        elif choice==2:
            power()
        elif choice==3:
            square_root()
        elif choice==4:
            percentage()
        elif choice==5:
            logarithmic()
        elif choice==6:
            exit()
        else:
            print("wrong choice")
if __name__=="__main__":
    main()