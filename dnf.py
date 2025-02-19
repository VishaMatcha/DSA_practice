def dnfalg(n):
    low=0
    mid=0
    high=len(n)-1
    while mid<high:
        if n[mid]==0:
            n[low],n[mid] = n[mid],n[low]
            low+=1
            mid+=1
        elif n[mid]==1:
            mid+=1
        else:
            n[high],n[mid]=n[mid],n[high]
            high-=1
            
    return n

n=[0,1,2,0,1,2,2,1,0]
print(dnfalg(n))