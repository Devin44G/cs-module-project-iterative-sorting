def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        middle = (begin + end) // 2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            end = middle - 1
        else:
            begin = middle + 1

    return -1  # not found
