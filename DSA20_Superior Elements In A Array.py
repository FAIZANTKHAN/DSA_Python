def superiorElements(arr: list[int]) -> list[int]:
    n = len(arr)  # Get the length of the input list
    i = n - 1  # Initialize a pointer to the last index
    ans = []  # Initialize an empty list to store superior elements
    mx = -float('inf')  # Initialize a variable to track the maximum value

    while i >= 0:  # Iterate from the last index to the first
        if arr[i] > mx:  # If the current element is greater than the maximum
            ans.append(arr[i])  # Add it to the answer list
            mx = arr[i]  # Update the maximum value
        i -= 1  # Move the pointer to the left

    return ans  # Return the list of superior elements


# Example usage:
input_array = [1, 2, 3, 2]
result = superiorElements(input_array)
print("Superior elements:", result)
