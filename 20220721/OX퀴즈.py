import sys

a = int(sys.stdin.readline())
for i in range(a):
    b = input()
    sum = 0
    count = 0

    for j in range(len(b)):
        if b[j] == 'O':
            count += 1
            sum += count
        elif b[j] == 'X':
            count = 0
            sum += 0

    print(sum)