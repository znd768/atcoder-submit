n, p, q = map(int, input().split())
dl = list(map(int, input().split()))
ans = p
for price in dl:
    ans = min(ans, price+q)
print(ans)