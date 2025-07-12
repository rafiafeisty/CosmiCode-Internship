def reversing():
    listing=input("Enter the list separated by spaces: ")
    listing=list(map(str,listing.strip().split()))
    reverse=[]
    for i in range(len(listing)-1,-1,-1):
        reverse.append(listing[i])
    print("Original List: ", listing)
    print("Reversed List: ", reverse)
print("REVERSING LIST")
reversing()