from typing import List
def linearSearch(array, key):
    """
    Perform linear search iteratively on the given array.

    Args:
        array (list): The input array.
        key (int): The target element to search for.

    Returns:
        int: Index of the target element if found, otherwise -1.
    """
    for i in range(len(array)):
        if array[i] == key:
            # Element found, return its index
            return i
    # Element not found
    return -1

# Example usage:
arr1_to_search = [1, 3, 5, 6, 7, 8]
target_num1 = 6
result = linearSearch(arr1_to_search, target_num1)
if result != -1:
    print(f"Index of {target_num1} in the array: {result}")
else:
    print(f"{target_num1} not found in the array.")





    

#Approach 2:Recursion
def helper(arr, i, n, k):
    """
    Recursive helper function for linear search.
    
    Args:
        arr (list): The input array.
        i (int): Current index.
        n (int): Length of the array.
        k (int): The target element to search for.
    
    Returns:
        int: Index of the target element if found, otherwise -1.
    """
    if i == n:
        # Base case: Element not found
        return -1
    if arr[i] == k:
        # Base case: Element found
        return i
    else:
        # Recursive case: Continue searching
        return helper(arr, i + 1, n, k)

def linearSearch(n: int, num: int, arr: List[int]) -> int:
    """
    Perform linear search on the given array.
    
    Args:
        n (int): Length of the array.
        num (int): The target element to search for.
        arr (list): The input array.
    
    Returns:
        int: Index of the target element if found, otherwise -1.
    """
    return helper(arr, 0, n, num)

# Example usage:
arr_to_search = [10, 20, 30, 40, 50]
target_num = 30
result = linearSearch(len(arr_to_search), target_num, arr_to_search)
print(f"Index of {target_num} in the array: {result}")
