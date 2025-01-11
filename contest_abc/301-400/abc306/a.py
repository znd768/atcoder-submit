n = int(input())
s = input()
print("".join([s[i]+s[i] for i in range(n)]))