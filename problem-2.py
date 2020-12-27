result = 0
a = 1
b = 2
tmp = 0
while b < 4000000:
    if (b % 2 == 0):
        result += b
    tmp = b + a
    a = b
    b = tmp
print(result)
