
import queue

def solve(arr,k):
    ele = queue.queue()
    for i in range(k):
        if arr[i]<0:
            ele.enqueue(arr[i])
    print(ele)
    
    
    start = 0 
    end = k-1
    
    ans = []
    if ele.isEmpty():
        ans.append(0)
    else:
        ans.append(arr[0])
    
    print(ans)
    while end < len(arr)-1:
        if arr[start] < 0:
            ele.dequeue()
        start += 1
        end += 1
        if arr[end]<0:
            ele.enqueue(arr[end])
            
        ans.append(ele.front())
        
        if ele.isEmpty():
            ans.append(0)
        else:
            ans.append(ele.front())
    
    return ans
    
arr = [2,-8,-10,4]
k = 2
print(solve(arr,k))        