def displaying():
    numbers=[]
    for i in range(3):
        numbers.append(float(input("Enter "+ str(i+1)+ " number: ")))
    smallest=numbers[0]
    largest=numbers[0]
    for i in range(3):
        if smallest>numbers[i]:
            smallest=numbers[i]
        if largest<numbers[i]:
            largest=numbers[i]
    print()
    print("smallest number: ", smallest)
    print("largest number: ",largest)

displaying()