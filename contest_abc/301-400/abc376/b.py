def f(n, s, t, x) :
  if s > t :
    s, t = t, s
  if s < x and x < t :
    return n - (t - s)
  else :
    return t - s
  
n, q = map(int, input().split())
commands = [list(input().split()) for _ in range(q)]
left = 0
right = 1
ans = 0
for i in range(q) :
  direction, position = commands[i]
  position = int(position) - 1
  if direction == "L" :
    ans += f(n, left, position, right)
    left = position
  else :
    ans += f(n, right, position, left)
    right = position
print(ans)