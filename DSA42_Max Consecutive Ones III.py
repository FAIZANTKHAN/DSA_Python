def longestOnes(arr: list[int], k: int) -> int:
    n = len(arr)
    s, e = 0, 0  # Initialize two pointers for the sliding window
    ans = 0  # Initialize the maximum length of consecutive 1s
    zero = 0  # Count of zeros in the current window
    one = 0  # Count of ones in the current window

    while e < n:
        if arr[e] == 1:
            one += 1
        else:
            zero += 1

        # If the number of zeros in the window is within the allowed limit (k),
        # update the maximum length encountered so far
        if zero <= k:
            ans = max(ans, e - s + 1)
            e += 1
        else:
            # Shrink the window from the left by incrementing 's'
            while s <= e and zero > k:
                if arr[s] == 1:
                    one -= 1
                else:
                    zero -= 1
                    s += 1

                # Update the maximum length if the adjusted window is valid
                if s <= e and zero <= k:
                    ans = max(ans, e - s + 1)
                    e += 1

    return ans

# Example usage:
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
result = longestOnes(nums, k)
print(f"Maximum consecutive 1s after flipping at most {k} zeros: {result}")
