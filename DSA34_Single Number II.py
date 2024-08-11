def elementThatAppearOnce(arr):
    # Initialize the answer to 0
    ans = 0
    
    # Iterate over each bit position (0 to 31 for a 32-bit integer)
    for i in range(32):
        cnt = 0  # Initialize the count of set bits at position i
        
        # Count the number of elements with the i-th bit set
        for item in arr:
            if item & (1 << i):
                cnt += 1
        
        # If the count of set bits at position i is not a multiple of 3,
        # it means the single number has a set bit at this position
        if cnt % 3 == 1:
            ans = ans | (1 << i)
    
    # Return the single number
    return ans

# Example usage
arr = [2, 2, 3, 2]
print(elementThatAppearOnce(arr))  # Output should be 3
