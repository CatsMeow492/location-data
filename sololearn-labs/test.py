import math
def SumOfSquares(N):
    
    #this is default OUTPUT. You can change it.
    result= []
    
    # write your Logic here:
    for num in list(N):
        if math.sqrt(int(num))/math.sqrt(int(num)) == 1:
            result.append(int(num))
    return sum(result)

# INPUT [uncomment & modify if required]
N = [1, 3, 36, 40, 43, 54, 64]

def checker(N):
    for num in list(N):
        i


# OUTPUT [uncomment & modify if required]
print(SumOfSquares(N))