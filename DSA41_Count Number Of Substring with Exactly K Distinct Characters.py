def atMostChar(name, k):
    # Get the length of the input string
    n = len(name)
    
    # Initialize start (s) and end (e) pointers for the sliding window
    s, e = 0, 0
    
    # Dictionary to keep track of character counts in the current window
    dp = {}
    
    # Variable to store the result
    ans = 0
    
    # Iterate over the string with the end pointer
    while e < n:
        # Get the current character at the end pointer
        ch = name[e]
        
        # Increment the count of the current character in the dictionary
        dp[ch] = dp.get(ch, 0) + 1
        
        # If the number of distinct characters in the window is less than or equal to k
        if len(dp) <= k:
            # Add the number of substrings ending at 'e' and starting from 's' to 'ans'
            ans = ans + e - s + 1
            # Move the end pointer to the right
            e += 1
        else:
            # If the number of distinct characters exceeds k
            while s <= e and len(dp) > k:
                # Get the character at the start pointer
                start_char = name[s]
                
                # Decrement the count of the start character
                if dp[start_char] > 1:
                    dp[start_char] -= 1
                else:
                    # If the count becomes 0, remove the character from the dictionary
                    del dp[start_char]
                
                # Move the start pointer to the right
                s += 1
            
            # After adjusting the start pointer, add the number of valid substrings
            if s <= e and len(dp) <= k:
                ans = ans + e - s + 1
            
            # Move the end pointer to the right
            e += 1
    
    # Return the total count of substrings with at most k distinct characters
    return ans


# Example input
name = "abcba"
k = 2

# Call the function and print the result
print(atMostChar(name, k))  # Expected output: 7


