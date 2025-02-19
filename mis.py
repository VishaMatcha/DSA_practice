def solve(arr):
    repeat = -1
    missing = -1
    currsum = 0
    totalsum = (len(arr)*(len(arr)+1))//2
    
    print(totalsum)
    
    for i in range(len(arr)):
        if arr[abs(arr[i])-1]<0:
            repeat = abs(arr[i])
        arr[abs(arr[i])s - 1] *= -1
        print("arr[i]",arr[i])
        currsum += abs(arr[i])
        
        print(currsum)
        
    missing = totalsum - (currsum-repeat)
    
    print("repeating : ", repeat," missing : ",missing)
    
arr = [1,2,3,4,1]
solve(arr)
