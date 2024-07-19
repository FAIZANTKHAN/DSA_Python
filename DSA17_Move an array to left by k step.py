def reverse(arr, s, e):
    # Reverses the elements in the array from index 's' to 'e'
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    # Reverse the entire array
    reverse(arr, 0, n - 1)
    # Reverse the first 'n-k' elements
    reverse(arr, 0, n - k - 1)
    # Reverse the last 'k' elements
    reverse(arr, n - k, n - 1)
    return arr


# Given array
arr = [1, 2, 3, 4, 5]
k = 2

# Apply left rotation
result = rotateArray(arr, k)

# Display the rotated array
print("Rotated array:", result)
