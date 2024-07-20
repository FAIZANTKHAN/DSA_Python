#Given a array of size n with equal pos and neg element
#Return ann element with alternate pos and neg element starting with pos without changing order

from typing import List

def alternateNumbers(arr: List[int]) -> List[int]:
    n = len(arr)
    ans = [0] * n
    positive_index, negative_index = 0, 1
    
    for item in arr:
        if item < 0:
            ans[negative_index] = item
            negative_index += 2
        else:
            ans[positive_index] = item
            positive_index += 2
    
    return ans

# Example usage:
input_array = [1, -2, 3, -4, 5, -6]
output_array = alternateNumbers(input_array)
print(output_array)  # Expected output: [1, -2, 3, -4, 5, -6]
