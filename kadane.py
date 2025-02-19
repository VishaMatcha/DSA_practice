#largest subarray sum

import sys

def maxconsum(a):
    start = 0
    end = 0
    maxsum = -sys.maxsize -1
    currsum = 0
    
    n = len(a)
    
    while end<n:
        while currsum < 0:
            currsum -= a[start]
            start += 1
            
        currsum += a[end]
        end += 1
        
        maxsum = max(maxsum, currsum)
    return maxsum

ls=[-1,1,2,3,4,5,-2,6,-3]
print("Max sum",maxconsum(ls))