#Approach 1
def total_sum_xor_pairs1(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            total_sum += arr[i] ^ arr[j]
    return total_sum

# Example usage
arr = [1, 2, 3]
print(total_sum_xor_pairs(arr))  # Output: 6


#Approach 2
def total_sum_xor_pairs2(arr):
    total_sum = 0
    n = len(arr)
    
    for bit in range(32):  # Assuming 32-bit integers
        bit_count = 0
        
        # Count the numbers with the current bit set
        for num in arr:
            if num & (1 << bit):
                bit_count += 1
        
        # Calculate pairs where one number has the bit set and the other does not
        pairs = bit_count * (n - bit_count)
        
        # Each such pair contributes 2^bit to the total sum
        total_sum += pairs * (1 << bit)
    
    return total_sum

# Example usage
arr = [1, 2, 3]
print(total_sum_xor_pairs(arr))  # Output: 6
