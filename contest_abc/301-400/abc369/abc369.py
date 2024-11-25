#A
# a, b = map(int, input().split())
# if a == b :
#   ans = 1
# elif (a + b) / 2 == (a + b) // 2:
#   ans = 3
# else:
#   ans = 2
# print(ans)

#B
# n = int(input())
# l = [list(input().split()) for _ in range(n)]
# ans = 0
# left_h = 0
# right_h = 0
# for i in range(n):
#   place, h = l[i]
#   place = int(place)
#   if h == "R" and right_h == 0 :
#     right_h = place
#   elif h == "L" and left_h == 0:
#     left_h = place
#   elif h == "R" :
#     ans += abs(right_h - place)
#     right_h = place
#   else:
#     ans += abs(left_h - place)
#     left_h = place
# print(ans)

#C
# import math
# n = int(input())
# al = list(map(int, input().split()))
# ans = n
# left_cursor = 0
# while left_cursor < n - 1:
#   right_cursor = left_cursor + 1
#   diff = al[right_cursor] - al[left_cursor]
#   elems = 2
#   while right_cursor < n - 1 and diff == al[right_cursor + 1] - al[right_cursor] :
#     right_cursor += 1
#     elems += 1
#   ans += math.comb(elems, 2)
#   left_cursor = right_cursor
# print(ans)

#D
n = int(input())
al = list(map(int, input().split()))
experience_val = 0
dp = [0 for _ in range(n)]
if n == 1:
  print(al[0])
  exit()
dp[0] = al[0], False
dp[1] = al[0] + al[1] * 2, True
for i in range(2, n):
  if dp[i - 2][1] and dp[i - 1][1]:
    dp[i] = max(dp[i - 2][0], dp[i - 1][0]) + al[i], False
  elif dp[i - 2][1]:
    if dp[i - 2][0] + al[i] > dp[i - 1][0] + al[i] * 2:
      dp[i] = dp[i - 2][0] + al[i], False
    else:
      dp[i] = dp[i - 1][0] + al[i] * 2, True
  elif dp[i - 1][1]:
    if dp[i - 1][0] + al[i] > dp[i - 2][0] + al[i] * 2:
      dp[i] = dp[i - 1][0] + al[i], False
    else:
      dp[i] = dp[i - 2][0] + al[i] * 2, True
  else:
    dp[i] = max(dp[i - 2][0], dp[i - 1][0]) + al[i] * 2, True
print(dp[-1][0])