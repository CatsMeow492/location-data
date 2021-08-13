def calc(x):
    a = x * x
    p = 4 * x
    return p, a
    

side = int(input())
p, a = calc(side)


   

print("Perimeter: " + str(p))
print("Area: " + str(a))