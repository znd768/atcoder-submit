s = input()
s = s[::-1]
print(''.join(['6' if c == '9' else '9' if c == '6' else c for c in s]))