def twosum(n,k):
    n.sort()
    start=0
    end=len(n)-1
    while start<end:
        sum = n[start]+n[end]
        if sum==k:
            return n[start],n[end]
        elif sum>k:
            end-=1
        elif sum<k: 
            start+=1
    return -1

n=[1,7,5,2,10]
k=6
print(twosum(n,k))