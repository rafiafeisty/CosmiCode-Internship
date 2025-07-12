def hanoi(n,fro,to,aux):
    if n==0:
        return
    hanoi(n-1,fro,aux,to)
    print("Moving disk ",n," from ",fro," to ", to)
    hanoi(n-1,aux,to,fro)
print("Tower of Hanoi")
hanoi(3,'A','C','B')