def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n&1) == 0:
        return False
    else:
        i = 0
        while(i*i < n):
            i+= 1
        for each in range(2,i+1):
            if n % each == 0:
                return False
        return True
        
n = int(input().strip())
if isPrime(n):
    print("Prime")
else:
    print("Not prime")