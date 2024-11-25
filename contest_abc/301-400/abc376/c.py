n = int(input())
toy = sorted(map(int, input().split()))
box = sorted(map(int, input().split()))
ans = toy[0]
used_wildcard = False
possible = True
for i in range(n):
  if used_wildcard:
    if toy[i] > box[i - 1]:
      possible = False
      break
  else:
    if i != n -1 and toy[i] > box[i]:
      used_wildcard = True
      ans = toy[i]
    elif toy[i] > box[i - 1]:
      ans = toy[i]
print(ans) if possible else print(-1)