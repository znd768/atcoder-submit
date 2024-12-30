year = int(input())
if year % 4 != 0:
    ans = 365
elif year % 100 != 0:
    ans = 366
elif year % 400 != 0:
    ans = 365
else:
    ans = 366
print(ans)