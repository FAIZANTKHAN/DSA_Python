#Max Array With K Sums
from typing import List

class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with 0 sum having one count
        ans = 0
        
        for i in range(n):
            prefix_sum += arr[i]  # Update the prefix sum
            rem = prefix_sum - k  # Calculate the remaining sum needed
            
            # If rem is in the prefix_sum_count, it means there is a subarray ending at i with sum k
            ans += prefix_sum_count.get(rem, 0)
            
            # Update the count of the current prefix_sum in the hash map
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        
        return ans

# Example usage:
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Output: 2

