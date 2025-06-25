def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    gcd1=gcd(a,b)
    lcm1=(a*b)/gcd1
    print("LCM of ",a,"and",b,"is",lcm1)

print("CALCULATING GCD AND LCM")   
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The GCD of",num1,"and",num2,"is: ",gcd(num1,num2))
lcm(num1,num2)