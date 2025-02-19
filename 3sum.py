def threesum(n,t):
    n.sort()
    for k in range(0,len(n)):
        temp = t
        temp -= n[k]
        start=k+1
        end=len(n)-1
        while start<end:
            sum = n[start]+n[end]
            if sum==temp:
                return n[k],n[start],n[end]
            elif sum>temp:
                end-=1
            elif sum<temp: 
                start+=1
    return -1

n=[1,7,5,2,10]
k=18
print(threesum(n,k))