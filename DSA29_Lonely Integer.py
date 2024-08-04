#Lonely Integer
def lonelyInteger(arr):
    ans = 0
    for item in arr:
        ans ^= item
    return ans


example_array = [1, 2, 3, 3,5,2, 1]
result = lonelyInteger(example_array)
print("Lonely Integer:", result)

