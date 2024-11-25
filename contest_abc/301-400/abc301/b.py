n = int(input())
a_l = list(map(int, input().split()))
output = []
for i, val in enumerate(a_l):
  if i == 0 or abs(val - output[-1]) == 1:
    output.append(val)
    continue
  if val > a_l[i - 1]:
    output.extend(list(range(a_l[i - 1]+1, val+1)))
  else:
    output.extend(list(range(a_l[i - 1]-1, val-1, -1)))
print(*output)