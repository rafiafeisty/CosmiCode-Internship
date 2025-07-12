def frequent():
    with open("file.txt") as file:
        array=file.read()
    listing=list(map(str,array.strip().split()))
    diction={}
    for i in range(len(listing)):
        word=listing[i]
        if word in diction:
            diction[word]+=1
        else:
            diction[word]=1
    frequent_word=max(diction,key=diction.get)
    print("Frequent word in the file: ", frequent_word)
print("FINDING FREQUENT WORD")
frequent()