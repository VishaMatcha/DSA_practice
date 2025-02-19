import math

def mva(n):
    maj=-1
    cnt=0
    
    for i in n:
        if cnt ==0:
            maj = i
            cnt =1
        else:
            if maj == i:
                cnt += 1
            else:
                cnt -= 1
    cnt=0
    for i in n:
        if maj == i:
            cnt += 1
    
    if cnt < len(n)//2:
        return -1
    else:
        return maj

n=[1,2,3,2,1]
print(mva(n))
print(math.floor(3/2))
print(math.ceil(3/2))
print(3//2)