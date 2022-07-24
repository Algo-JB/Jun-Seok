import sys

a=[]
mul = 1
for i in range(3):
    a.append(int(sys.stdin.readline()))
    mul *= a[i]


y = [int(a) for a in str(mul)]

for i in range(10):
    print(y.count(i))