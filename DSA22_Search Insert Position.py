def find_index(arr, target):
    # Initialize the start and end pointers for binary search.
    start, end = 0, len(arr) - 1
    
    # Perform binary search until the start pointer is less than or equal to the end pointer.
    while start <= end:
        # Calculate the middle index.
        mid = (start + end) // 2
        
        # Check if the middle element equals the target.
        if arr[mid] == target:
            return mid
        # If the middle element is less than the target, update the start pointer.
        elif arr[mid] < target:
            start = mid + 1
        # Otherwise, update the end pointer.
        else:
            end = mid - 1
    
    # If the loop completes without finding the target, return the correct insert position.
    return end + 1

# Example usage:
arr = [1, 3, 5, 6]
K = 2
print(find_index(arr, K))  # Output: 1

