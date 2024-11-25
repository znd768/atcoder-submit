s = input()
l = [len(x) for x in s[1:-1].split('|')]
print(*l)