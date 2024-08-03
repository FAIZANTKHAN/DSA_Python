#Check no. of set bits
#Approach 1
def countSetBits(n):
    cnt = 0
    while n > 0:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt

# Example usage
number = 9
print(countSetBits(number))  # Output: 2



#Approach 2
def countSetBits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n = n & (n - 1)
    return cnt

# Example usage
number = 15
print(countSetBits(number))  # Output: 2
