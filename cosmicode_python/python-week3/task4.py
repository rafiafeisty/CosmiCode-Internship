def palindrome():
    str=input("Enter a string: ")
    str=str.strip()
    str=str.lower()
    reverse=""
    for i in range(len(str)-1,-1,-1):
        reverse+=str[i]
    if str==reverse:
        print("Entered string is palindrome")
    else:
        print("String is not palindrome")
print("PALINDROME CHECKING")
palindrome()