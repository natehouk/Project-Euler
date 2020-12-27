answer = 20
while True:
    for i in range(1, 21):
        if (answer % i != 0):
            break
        elif (i == 20):
            print(answer)
            exit()
    answer += 20
