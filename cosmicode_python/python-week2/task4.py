import math
def check_prime(n):
    sq=math.sqrt(n)
    for i in range(2,int(sq)+1):
        if n%i==0:
            return False
            
    return True

def printing_prime():
    num = int(input("Enter a number: "))
    div=2
    num1=[]
    while(num!=1):
        if(num%div==0):
            num1.append(div)
            num=num//div
            div=2
        else:
            div+=1
    sorted(num1)
    for i in range(len(num1)):
        if check_prime(int(num1[i])):
            print(num1[i], end=" ")
print("PRINITING PRIME FACTORS")
printing_prime()