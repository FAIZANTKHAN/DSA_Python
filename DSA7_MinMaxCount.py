mxCount=0
mxValue=None
mnCount=1000
mnValue=None
d = {'a': 10, 'b': 20, 'c': 5}

for key,count in d.items():
    if mxCount<count:
        mxValue=key
        mxCount=count
    if mnCount>count:
        mnValue=key
        mnCount=count

print(f"Maximum value: {mxValue} ({d[mxValue]})")
print(f"Minimum value: {mnValue} ({d[mnValue]})")
