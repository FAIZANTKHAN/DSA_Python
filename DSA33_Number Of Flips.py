#Number of Flips

#eg:    a=10111011
#       b=01010011 so,number of flips required to a=b is 4

#Approach 1

def numberOfFlips(a: int, b: int) -> int:
    cnt = 0  # Initialize the count of flips to 0
    for i in range(32):  # Iterate over each bit position (assuming 32-bit integers)
        # Extract the i-th bit of 'a'
        bitA = 1 if a & (1 << i) else 0
        # Extract the i-th bit of 'b'
        bitB = 1 if b & (1 << i) else 0
        
        # If the bits are different, increment the count
        if bitA != bitB:
            cnt += 1
    return cnt  # Return the total count of flips


a = 0b10111011  # Binary representation of 187
b = 0b01010011  # Binary representation of 83

print(numberOfFlips(a, b))  # Output should be 4


#Approach 2

def numberOfFlips1(a: int, b: int) -> int:
    cnt = 0  # Initialize the count of flips to 0
    c = a ^ b  # XOR a and b to get a number where each bit is 1 if the corresponding bits of a and b are different
    while c > 0:  # Loop until all bits are processed
        c = c & (c - 1)  # Remove the rightmost set bit from c
        cnt += 1  # Increment the count of flips
    return cnt  # Return the total count of flips

a = 0b10111011  # Binary representation of 187
b = 0b01010011  # Binary representation of 83

print(numberOfFlips1(a, b))  # Output should be 4


