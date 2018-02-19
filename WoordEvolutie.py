s = input()
c = input().lower()[0]
i = ord(c) - ord(s.lower()[0])
new_s = ''
for a in s:
    new_s+=chr(ord(a)+i)
print(new_s)