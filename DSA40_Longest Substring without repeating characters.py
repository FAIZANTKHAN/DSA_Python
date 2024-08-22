def lengthOfLongestSubstring(name: str) -> int:
    n = len(name)  # Length of the input string
    s, e = 0, 0  # Start and end pointers for the sliding window
    dp = {}  # Dictionary to store the count of characters in the current window
    ans = 0  # Variable to store the length of the longest substring without repeating characters

    while e < n:
        ch = name[e]  # Current character at the end pointer
        dp[ch] = dp.get(ch, 0) + 1  # Increment the count of the current character

        # If the current window has all unique characters
        if len(dp) == e - s + 1:
            ans = max(ans, e - s + 1)  # Update the answer with the maximum length found
            e += 1  # Move the end pointer to the right
        else:
            # If there are repeating characters in the current window
            while s <= e and len(dp) != e - s + 1:
                ch = name[s]  # Current character at the start pointer
                if dp[ch] > 1:
                    dp[ch] -= 1  # Decrement the count of the character
                else:
                    del dp[ch]  # Remove the character from the dictionary if its count is 1
                s += 1  # Move the start pointer to the right
            if s <= e and len(dp) == e - s + 1:
                ans = max(ans, e - s + 1)  # Update the answer with the maximum length found
            e += 1  # Move the end pointer to the right

    return ans  # Return the length of the longest substring without repeating characters

# Example input
input_string = "abcabcbb"
# Expected output: 3 (The longest substring without repeating characters is "abc")
# Instantiate the class and call the method

print(lengthOfLongestSubstring(input_string))  # Output: 3
