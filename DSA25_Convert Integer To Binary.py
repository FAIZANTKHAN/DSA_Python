def intToBinary(num: int) -> str:
    ans = ""  # Initialize an empty string to store the binary representation
    while num > 0:
        r = num % 2  # Calculate the remainder when dividing by 2
        ans += str(r)  # Append the remainder (0 or 1) to the answer string
        num = num // 2  # Update the number by integer division (floor division) by 2
    return ans[::-1]  # Reverse the answer string to get the correct binary representation

print(intToBinary(23))

