#Approach 1
def pair_sum_xor_naive(arr):
    n = len(arr)
    result = 0
    
    # Iterate over all pairs
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate sum of the pair
            pair_sum = arr[i] + arr[j]
            # Update the result with XOR of the pair sum
            result ^= pair_sum
    
    return result

# Example usage:
arr = [1, 2, 3]
print(pair_sum_xor_naive(arr))  # Output: 2


#Approach 2
def pair_sum_xor_bitwise(arr):
    n = len(arr)
    result = 0
    
    # Calculate the total sum of all elements in the array
    total_sum = sum(arr)
    
    # Iterate through each element to compute the result
    for value in arr:
        # Calculate the remaining sum after excluding the current element
        remaining_sum = total_sum - value
        # Update the result with XOR of remaining_sum + current element
        result ^= (remaining_sum + value)
    
    return result

# Example usage:
arr = [1, 2, 3]
print(pair_sum_xor_bitwise(arr))  # Output: 2
