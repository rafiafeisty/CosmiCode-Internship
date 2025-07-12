def binary_search():
    arr=input("Enter the numbers separated by space: ")
    n=int(input("Enter the target number: "))
    arr=list(map(int,arr.strip().split()))
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==n:
            print("Index of the target element: ",mid)
            return
        else:
            if arr[mid]>n:
                right=mid-1
            else:
                left=mid+1
    print("Targest number doesn't exist")
    
print("BINARY SEARCH")
binary_search()