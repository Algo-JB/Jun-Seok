a = int(input())

count = 0
if a < 100:
    print(a)

if a >= 100:

    for i in range(100, a+1):
        y = [int(x) for x in str(i)]

        if (y[1] - y[0]) == (y[2] - y[1]):
            count += 1
        elif (y[0] - y[1]) == (y[1] - y[2]):
            count+= 1
    print(count + 99)