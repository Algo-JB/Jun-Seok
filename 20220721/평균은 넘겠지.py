import sys

a = int(sys.stdin.readline())

for i in range(a):
    b = list(map(int, sys.stdin.readline().split( )))

    c = b[0]
    b.pop(0)
    avg = sum(b) / c
    count = 0
    for i in range(len(b)):
        if b[i] > avg:
            count += 1
    x = round((count / c) * 100, 3)
    print(f"{x:.3f}%")