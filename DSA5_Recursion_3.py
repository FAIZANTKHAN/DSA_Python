#Recursion 3
    #Reverse an Array(Two Pointer)


lst=list(map(int,input().split()))
n=len(list)

#Loop appproach
for i in range(n//2):
    lst[i],lst[n-1-i]=lst[n-1-i],lst[i]
    print(lst)

#or

#Two Pointer
s=0
e=n-1
while s<=e:
    lst[s],lst[e]=lst[e],lst[s]
    s+=1
    e-=1
    print(lst)

#Two Pointer(Recursive Approach)

def reverse(s,e,lst):
    if s<e:
        return
    lst[s],lst[e]=lst[e],lst[s]
    reverse(s+1,e-1,lst)
