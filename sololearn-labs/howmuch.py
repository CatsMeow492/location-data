price = int(input())
perc = int(input())

res = (lambda x,y:((perc)/100)*price)(price,perc)

print(res)