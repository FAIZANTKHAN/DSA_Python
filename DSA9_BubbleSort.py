from typing import List

def bubbleSort(arr:List[int],n:int):
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def bubbleSort(arr:List[int],n:int):
    for i in range(n):
        isSorted=True
        for j in range(n-i-1):
            if arr[j]>arr[j-1]:
                isSorted=False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if isSorted:
            break
    return arr