def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    list = []

    while a < b:
        list.append(a)
        if isPrime(a):
            yield a
        a += 1


    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))