# s = str(input())

# x = [-1] * 26

# for i in s:
#     if ord(i) >= 97 or ord(i) <= 122:
#         x[ord(i) - 97] = s.index(i) 
    
# print(x)    

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)))