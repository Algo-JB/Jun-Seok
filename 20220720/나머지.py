import sys
a = []
b = []
for i in range(10):
    a.append(int(sys.stdin.readline()))
    b.append(a[i] % 42)

b = set(b)
print(len(b))