# Using Iterative Approach
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

# Using Recursive Approach
def helper(arr, ind):
    if ind == 0:
        return
    helper(arr, ind - 1)
    while ind > 0 and arr[ind] < arr[ind - 1]:
        arr[ind], arr[ind - 1] = arr[ind - 1], arr[ind]
        ind -= 1

def recursiveInsertionSort(arr):
    n = len(arr)
    helper(arr, n - 1)

# Example usage
random_input = [5, 2, 9, 1, 5, 6]
sorted_output = insertionSort(random_input)
print("Sorted array using iterative approach:", sorted_output)

recursive_sorted_output = random_input.copy()
recursiveInsertionSort(recursive_sorted_output)
print("Sorted array using recursive approach:", recursive_sorted_output)
