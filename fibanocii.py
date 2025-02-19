def fibanocii(n):
    if n==0 or n==1:
        return 1
    
    return fibanocii(n-1)+fibanocii(n-2)

print(fibanocii(6))
        