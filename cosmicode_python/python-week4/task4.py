def frequent():
    array=input("Enter the string: ")
    diction={}
    for i in range(len(array)):
        word=array[i]
        if word in diction:
            diction[word]+=1
        else:
            diction[word]=1
    for key,value in diction.items():
        print(key, ": ",value)
print("FINDING FREQUENCY")
frequent()