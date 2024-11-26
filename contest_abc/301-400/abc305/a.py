n = int(input())
d, m = divmod(n, 5)
print(d*5 if m < 3 else (d+1)*5)
