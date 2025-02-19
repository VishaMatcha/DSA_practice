import sys

def kadane(a):
    start = 0
    end =0
    maxsum = -sys.maxsize -1
    currsum =0
    
    while end<len(a):
        while currsum<0:
            currsum -= a[start]
            start += 1
            
        currsum += a[end]
        end += 1
        
        maxsum = max(maxsum, currsum)
    
    return maxsum
    

matrix = [[3,8,9,1,3],[-4,-1,1,7,-6],[-2,-3,8,1,-1]]

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize -1

for i in range (m):
    temp=[]
    for j in range (n):
        temp.append(matrix[j][i])
    
    print(temp)
    ans = max(ans,kadane(temp))
    print(ans)
    for j in range(i+1,m):
        for k in range(n):
            temp[k] += matrix[k][j]
            
        print(temp)
        ans = max(ans, kadane(temp))
        print(ans)
    print('--------------------------------------')
        
print(ans)