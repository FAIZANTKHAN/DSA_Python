#XOR Queries of Subarray
#Approach 1
def xorQueries(self,arr:list[int],queries:[list[int]])->list):
    ans=[]
    for l,r in queries:
        temp=0
        for i in range(1,r+1):
            temp=temp^arr[i]
        ans.append(temp)
    return ans

#Approach 2
def xorQueries(self,arr:list[int],queries:[list[int]])->list):
    n=len(arr)
    prefix=[0]*(n)
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]^arr[i]

    for l,r in queries:
        if l==0:temp=prefix[r]
        else:temp=prefix[r]^prefix[l-1]
        ans.append(temp)
    return ans
