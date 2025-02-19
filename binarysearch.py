def search(arr,t):
    b=0
    e=len(arr)
    while b<e:
        m=(b+e)//2
        if t==arr[m]:
            return True
        elif t>arr[m]:
            b=m
        else:
            e=m
    return False

arr=[1,2,3,4,5,6,7,8]
if search(arr,9):
    print("element present")
else:
    print("Element not present")    