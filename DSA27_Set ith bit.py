def setKthBit(n, i):
    return n | (1 << i)
# This sets the i-th bit of n to 1 if it was initially 0.
    # If the i-th bit of n is already 1, it remains unchanged.
number = 1011
bit_position = 2
result = setKthBit(number, bit_position)
print(f"Setting bit {bit_position} of {number} results in {result}.")
