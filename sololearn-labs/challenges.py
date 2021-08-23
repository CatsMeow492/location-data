print(len(set('1111'.split('1'))))
print(set('1111'.split('1')))

def power(x,y):
    if y== 0:
        return 1
    else:
        return x * power( x, y-1)

print(power(2,3))
