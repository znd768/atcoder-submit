from collections import OrderedDict
n, m = map(int, input().split())
idx_exists = list(map(int, input().split()))
value_list = list(map(int, input().split()))
# d = dict(zip(idx_exists, value_list))
# dd = OrderedDict(sorted(d.items()))
idx_order = sorted(list(range(m)), key=lambda x: idx_exists[x])
dd = {idx_exists[i]: value_list[i] for i in idx_order}

sum_value = 0
sum_idx = 0

for idx, value in dd.items():
  if sum_value < idx - 1:
    print(-1)
    exit()
  sum_value += value
  sum_idx += idx * value

if sum_value != n:
  print(-1)
  exit()

print(n * (n + 1) // 2 - sum_idx)



  