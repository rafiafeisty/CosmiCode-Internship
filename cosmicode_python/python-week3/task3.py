import string

def longest_word():
    user_input=input("Enter the sentence: ")
    listing=list(map(str,user_input.strip().split()))
    numbers=[]
    for i in range(len(listing)):
        word=listing[i]
        word=word.strip(string.punctuation)
        numbers.append(int(len(word)))
    max_num=max(numbers)
    max_index=0
    for i in range(len(numbers)):
        if max_num==int(numbers[i]):
            max_index=i
            break
    longest=listing[max_index]
    print("Longest word in the sentence: ", longest)
print("FINDING LONGEST WORD")
longest_word()