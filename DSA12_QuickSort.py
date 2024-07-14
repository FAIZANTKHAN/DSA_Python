import random

def pivotIndex(arr, s, e):
    pivot = arr[e]
    ind = s
    for i in range(s, e):
        if arr[i] < pivot:
            arr[i], arr[ind] = arr[ind], arr[i]
            ind += 1
    arr[ind], arr[e] = arr[e], arr[ind]
    return ind

def quickSort(arr, s, e):
    if s < e:
        pI = pivotIndex(arr, s, e)
        quickSort(arr, s, pI - 1)
        quickSort(arr, pI + 1, e)

# Generating a random array to test the quicksort function
arr = [random.randint(1, 100) for _ in range(10)]
print("Original array:", arr)
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
