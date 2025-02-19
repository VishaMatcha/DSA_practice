#largest subarray sum

import sys

def getnum(ch):
    if ch == "0":
        return 1
    return -1

def maxconsum(a):
    start = 0
    end = 0
    maxsum = -sys.maxsize -1
    currsum = 0
    cnt = 0
    
    for i in a:
        if i == "1":
            cnt += 1
    
    n = len(a)
    
    while end<n:
        while currsum < 0:
            currsum -= getnum(a[start])
            start += 1
            
        currsum += getnum(a[end])
        end += 1
        
        maxsum = max(maxsum, currsum)
    return maxsum + cnt

ls="0001"
print("Max sum",maxconsum(ls))