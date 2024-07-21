from typing import List

def nextGreaterPermutation(arr: List[int]) -> List[int]:
    n = len(arr)
    i = n - 1

    # Find the first element that is not in decreasing order from right
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    bridge = i - 1  # Index of the bridge element

    # If no greater permutation is possible, return the reversed array
    if bridge == -1:
        return arr[::-1]

    i = n - 1
    # Find the next element greater than the one at the bridge position
    while arr[i] <= arr[bridge]:
        i -= 1
    arr[i], arr[bridge] = arr[bridge], arr[i]

    # Reverse the suffix from bridge+1 to n-1
    reverse(arr, bridge + 1, n - 1)
    return arr

def reverse(arr: List[int], s: int, e: int) -> None:
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

# Example usage
input_array = [7,2,9,8,6]
result = nextGreaterPermutation(input_array)
print("Next greater permutation:", result)
