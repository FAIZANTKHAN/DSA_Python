#Prefix Sum Array

#Approach 1
def prefix_sum_query1(arr, l, r):
    # Get the length of the array
    n = len(arr)

    # Initialize the prefix sum array with zeros
    prefix = [0] * n

    # Calculate the prefix sum array
    for i in range(n):
        # If it's the first element, the prefix sum is the element itself
        if i == 0:
            prefix[i] = arr[i]
        else:
            # Otherwise, it's the current element plus the prefix sum of the previous element
            prefix[i] = arr[i] + prefix[i - 1]

    # Print the prefix sum array
    print("Prefix Sum Array:", prefix)

    # If the left index of the range is 0, the sum is just the prefix sum at the right index
    if l == 0:
        return prefix[r]
    else:
        # Otherwise, it's the difference between the prefix sums at the right and left-1 indices
        return prefix[r] - prefix[l - 1]

# Example usage
arr = [1, 2, 3, 4, 5, 6]
l = 2
r = 5
result = prefix_sum_query1(arr, l, r)
print("Subarray Sum:", result)



#Approach 2
def prefix_xor_query2(arr, l, r):
    # Get the length of the array
    n = len(arr)

    # Initialize the prefix XOR array with zeros
    prefix_xor = [0] * n

    # Calculate the prefix XOR array
    for i in range(n):
        # If it's the first element, the prefix XOR is the element itself
        if i == 0:
            prefix_xor[i] = arr[i]
        else:
            # Otherwise, it's the current element XORed with the prefix XOR of the previous element
            prefix_xor[i] = arr[i] ^ prefix_xor[i - 1]

    # Print the prefix XOR array
    print("Prefix XOR Array:", prefix_xor)

    # If the left index of the range is 0, the XOR is just the prefix XOR at the right index
    if l == 0:
        return prefix_xor[r]
    else:
        # Otherwise, it's the prefix XOR at the right index XORed with the prefix XOR at the left index - 1
        return prefix_xor[r] ^ prefix_xor[l - 1]

# Example usage
arr = [1, 2, 3, 4, 5, 6]
l = 2
r = 5
result = prefix_xor_query2(arr, l, r)
print("Subarray XOR:", result)
