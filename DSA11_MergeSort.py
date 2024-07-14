def mergeSort(arr: list, s: int, e: int):
    if s < e:
        mid = (s + e) // 2
        mergeSort(arr, s, mid)
        mergeSort(arr, mid + 1, e)

        left = arr[s:mid + 1]
        right = arr[mid + 1:e + 1]

        i, j, k = 0, 0, s  # Initialize indices for left, right, and merged array

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from left and right subarrays
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

# Example usage
random_input = [5, 2, 9, 1, 5, 6]
mergeSort(random_input, 0, len(random_input) - 1)
print("Sorted array using merge sort:", random_input)
