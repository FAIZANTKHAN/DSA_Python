def floorSqrt(n):
    # Initialize the search range: start (s) and end (e)
    s, e = 1, n
    # Initialize the answer (ans) to 1
    ans = 1
    # Binary search loop
    while s <= e:
        # Calculate the midpoint
        mid = (s + e) // 2
        # Check if mid^2 is less than or equal to n
        if mid <= n / mid:
            # Update the answer and move the search range to the right
            ans = mid
            s = mid + 1
        else:
            # Move the search range to the left
            e = mid - 1
    # Return the floor square root
    return ans

# Read an integer input from the user
n = int(input())
# Print the result of floorSqurt(n)
print(floorSqrt(n))
