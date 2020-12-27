sumOf = 0
squareOf = 0
for i in range (1, 101):
    sumOf += i*i
    squareOf += i
squareOf = squareOf * squareOf
print(squareOf - sumOf)
