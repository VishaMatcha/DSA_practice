from math import *

def rotate(arr,d):
    g = gcd(len(arr),d)
    print(g)
    
    for i in range(g):
        print(i)
        temp = arr[i]
        j = i
        while True:
            k = (j-d)%len(arr)
            print("j", j)
            print("k", k)
            if k == i:
                break
            
            arr[j] = arr[k]
            j = k             
            
        arr[j] = temp
        
    return arr

arr=[1,2,3,4,5]
print(rotate(arr,2))