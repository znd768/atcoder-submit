n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(lambda x: int(x) - 1, input().split()))

d = {}
for c in c_list:
  d[b_list[c]] = d.get(b_list[c], 0) + 1

ans = 0
for num in a_list:
  ans += d.get(num, 0)

print(ans)