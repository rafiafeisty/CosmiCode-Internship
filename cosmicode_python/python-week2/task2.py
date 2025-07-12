def fibonaaci_iterative():
    fib=[]
    fib.append(0)
    fib.append(1)
    for i in range(2,30):
        fib.append(fib[i-1]+fib[i-2])
    for i in range(len(fib)):
        print(fib[i],end=" ")

def fibonacci_recursive(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    else:
        return (fibonacci_recursive(n-1)+fibonacci_recursive(n-2))
    
def printing_recursive():
    for i in range(30):
        print(fibonacci_recursive(i),end=" ")

print("FIBONACCI ITERATIVE APPROACH")
fibonaaci_iterative()
print("\n")
print("FIBONACCI RECURSIVE APPROACH")
printing_recursive()