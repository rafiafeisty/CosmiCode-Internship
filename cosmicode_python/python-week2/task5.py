def kadane_algorithm(arr):
    max_sum = float('-inf') 
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    print("Maximum subarray sum is:", max_sum)
    print("Subarray is:", arr[start:end+1])

user_input = input("Enter a list of integers separated by spaces: ")
arr = list(map(int, user_input.strip().split()))
print("KADANE ALGORITHM")
kadane_algorithm(arr)
