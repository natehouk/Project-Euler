def is_palidrone(value):
    length = len(str(value))
    for i in range(0, length):
        if (str(value)[i] != str(value)[length-i-1]):
            return False
    return True

max_palidrone = 0
for i in range(999, 99, -1):
    for j in range (999, 99, -1):
        if (is_palidrone(i*j) and i*j > max_palidrone):
            max_palidrone = i*j
print max_palidrone
