n = int(input())

file = open("numbers.txt", "w+")
#your code goes here
for i in range(n):
    file.write(str(i + 1) + "\n")

print(file.read())
f = open("numbers.txt", "r")
print(f.read())
f.close()