def factorial(n):
    if (n < 1):
        raise Exception
    if (n == 1):
        return 1
    else:
        return n*factorial(n-1)

print(sum(int(digit) for digit in str(factorial(100))))