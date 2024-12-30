a,b,c,d = map(int, input().split())
if len({a,b,c,d}) == 2:
    print("Yes")
else:
    print("No")