def search(arr: list, target: int) -> int:
    n = len(arr)  # Get the length of the input array
    s, e = 0, n - 1  # Initialize start and end pointers for binary search

    while s <= e:  # Continue the search while start pointer is less than or equal to end pointer
        mid = (s + e) // 2  # Calculate the middle index
        if target < arr[mid]:  # If target is less than the middle element
            e = mid - 1  # Update end pointer to search the left half
        elif target > arr[mid]:  # If target is greater than the middle element
            s = mid + 1  # Update start pointer to search the right half
        else:  # If target is equal to the middle element
            return mid  # Return the index where target is found

    return -1  # Target not found, return -1


array = [3, 6, 7, 9, 21, 23, 55, 62]
target = 9
result = search(array, target)
if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not found.")
