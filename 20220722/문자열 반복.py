a = int(input())

for i in range(a):
    b, c = map(str, input().split())

    b = int(b)

    for i in c:
        print(i * b, end = '')
    print()
