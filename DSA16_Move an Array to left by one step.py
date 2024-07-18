def rotateArray(arr, n):
    # Store the first element of the array in a temporary variable
    temp = arr[0]
    
    # Iterate over the array from index 1 to n-1
    for i in range(1, n):
        # Shift each element one position to the left
        arr[i - 1] = arr[i]
    
    # Place the original first element at the end of the array
    arr[n - 1] = temp
    
    # Return the modified array
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
size = len(arr)
rotateArray(arr, size)
print("Rotated array:", arr)
