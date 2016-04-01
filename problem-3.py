magic = 600851475143
factors = []
i = 2
while True:
    if (magic % i == 0):
        factors.append(i)
        magic = magic / i
        i = 2
    else:
        i += 1
    if (i == magic):
        factors.append(i)
        break
factors = sorted(factors, reverse=True)
print factors[0]
