#Majority Element
#Approach-1:HashMap (Dictionary) Approach
def majorityElement1(nums: list[int]) -> int:
    # Create an empty dictionary to store the frequency of each element
    dp = {}
    n = len(nums)
    
    # Loop through each item in the nums list
    for item in nums:
        # Increment the count of the item in the dictionary
        dp[item] = dp.get(item, 0) + 1
    
    # Initialize the variable to store the majority element
    ans = None
    
    # Check the frequency of each element in the dictionary
    for k, v in dp.items():
        # If the frequency of the element is greater than n//2, it's the majority element
        if v > n // 2:
            ans = k
            break
    
    # Return the majority element
    return ans


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement1(nums))  # Output should be 2


#Approach-2:Sorting Approach
def majorityElement2(nums: list[int]) -> int:
    nums.sort()  # Sort the list
    n = len(nums)
    cnt = 0
    ele = None
    ans = None
    
    # Loop through each item in the sorted nums list
    for item in nums:
        if item == ele:
            cnt += 1  # Increment count if the item is the same as the previous one
        else:
            ele = item  # Update ele to the current item
            cnt = 1  # Reset count to 1
        
        # If count exceeds n//2, it's the majority element
        if cnt > n // 2:
            ans = ele
            break
    
    return ans

nums = [3, 2, 3]
print(majorityElement2(nums))  # Output should be 3



#Approach-3:Boyer-Moore Voting Algorithm
def majorityElement3(nums: list[int]) -> int:
    cnt = 0  # Initialize counter
    ele = None  # Initialize the majority element candidate
    
    # Loop through each item in nums
    for item in nums:
        if cnt == 0:
            ele = item  # Update the candidate when count is zero
            cnt = 1  # Reset count to 1
        elif ele == item:
            cnt += 1  # Increment count if the item matches the candidate
        else:
            cnt -= 1  # Decrement count if the item doesn't match the candidate
    
    # Return the candidate element as the majority element
    return ele


nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majorityElement3(nums))  # Output should be 4

