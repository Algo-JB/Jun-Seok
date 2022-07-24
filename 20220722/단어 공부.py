a = str(input())
a = a.lower()

b = [0] * 26

for i in a: 
    if ord(i) >= 97 or ord(i) <= 122:
        b[ord(i) -97] += 1
    x = chr(b.index(max(b)) + 1 + 64)
if b.count(max(b)) >= 2:
    x = '?'
print(x)