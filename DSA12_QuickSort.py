import random

# Function to find the pivot index for partitioning the array
def pivotIndex(arr, s, e):
    # Choose the pivot element (last element in this case)
    pivot = arr[e]
    # Initialize the index of smaller element
    ind = s
    # Loop through the array from start to end-1
    for i in range(s, e):
        # If the current element is smaller than the pivot
        if arr[i] < pivot:
            # Swap the current element with the element at index 'ind'
            arr[i], arr[ind] = arr[ind], arr[i]
            # Increment the index of the smaller element
            ind += 1
    # Swap the pivot element with the element at index 'ind'
    arr[ind], arr[e] = arr[e], arr[ind]
    # Return the index of the pivot element
    return ind

# Function to perform quicksort on the array
def quickSort(arr, s, e):
    # Base case: if start index is less than end index
    if s < e:
        # Find the pivot index
        pI = pivotIndex(arr, s, e)
        # Recursively sort elements before the pivot
        quickSort(arr, s, pI - 1)
        # Recursively sort elements after the pivot
        quickSort(arr, pI + 1, e)

# Generate a random array to test the quicksort function
arr = [random.randint(1, 100) for _ in range(10)]
print("Original array:", arr)
# Call quicksort on the entire array
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
