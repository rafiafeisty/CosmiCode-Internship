def merging(left,right):
    arr=[]
    i=0
    j=0
    while(i <len(left) and j <len(right)):
        if left[i]>right[j]:
            arr.append(right[j])
            j+=1
        else:
            arr.append(left[i])
            i+=1
    while(i<len(left)):
        arr.append(left[i])
        i+=1
    while(j<len(right)):
        arr.append(right[j])
        j+=1
    return arr


def breaking(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=[]
    right=[]
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid,len(arr)):
        right.append(arr[i])
    left=breaking(left)
    right=breaking(right)
    arr=merging(left,right)
    return arr


def merge_sort():
    user_input=input("Enter the numbers separated by commas: ")
    arr=list(map(int,user_input.strip().split(',')))
    arr=breaking(arr)
    print("Sorted Array: ",arr)

print("MERGE SORT")
merge_sort()