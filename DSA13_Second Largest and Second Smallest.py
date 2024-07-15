from typing import List

def getSecondOrderElement(arr: List[int]) -> List[int]:
    # Initialize variables to store the largest (l) and second largest (sl) elements,
    # as well as the smallest (s) and second smallest (ss) elements.
    l, sl, s, ss = float('-inf'), float('-inf'), float('inf'), float('inf')
    
    # Iterate through each item in the input array.
    for item in arr:
        # Update the largest and second largest elements.
        if item > l:
            sl = l
            l = item
        elif item > sl:
            sl = item
        
        # Update the smallest and second smallest elements.
        if item < s:
            ss = s
            s = item
        elif item < ss:
            ss = item
    
    # Return a list containing the second largest and second smallest elements.
    return [sl, ss]

# Example usage:
random_array = [5, 10, 3, 8, 2]
result = getSecondOrderElement(random_array)
print("Second largest and second smallest elements:", result)
