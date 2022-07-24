import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

sum = 0
for i in range(a):
    sum += b[i] / max(b) * 100

print(sum / a)
