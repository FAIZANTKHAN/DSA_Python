#Check that ith bit is set or not
def checkKthBit(n,i):
    return n&(1<<i)

# Perform a bitwise AND operation between n and (1<<i).
# If the result is non-zero, the k-th bit of n is set (1); otherwise, it is not set (0).


# Test with n = 23 and k = 2
print(checkKthBit(23, 2))
