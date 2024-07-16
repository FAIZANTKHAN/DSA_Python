def helper(arr, i):
    """
    Recursive helper function to check if the array is sorted in non-decreasing order.

    Args:
        arr (list): The input array.
        i (int): Current index being checked.

    Returns:
        int: 1 if the array is sorted, 0 otherwise.
    """
    if i == 0:
        # Base case: If we've reached the first element, return 1 (sorted).
        return 1
    # Check if arr[i] is greater than or equal to arr[i-1].
    # If so, continue checking the previous elements.
    return int(arr[i] >= arr[i - 1]) and helper(arr, i - 1)

def isSorted(n: int, arr: list[int]) -> int:
    """
    Determines if the input array is sorted in non-decreasing order.

    Args:
        n (int): Length of the array.
        arr (list): The input array.

    Returns:
        int: 1 if the array is sorted, 0 otherwise.
    """
    return helper(arr, n - 1)

# Example usage:
input_array = [1, 2, 3, 5, 5, 7]
result = isSorted(len(input_array), input_array)
print(f"Is the array sorted? {result}")
