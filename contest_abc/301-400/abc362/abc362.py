#A
# r, g, b = map(int, input().split())
# c = input()
# match (c) :
#   case 'Red':
#     print(min(g, b))
#   case 'Green':
#     print(min(r, b))
#   case 'Blue':
#     print(min(r, g))

#B
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# e1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
# e2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
# e3 = (x3 - x1) ** 2 + (y3 - y1) ** 2
# el = sorted([e1, e2, e3], reverse=True)
# if (el[0] == el[1] + el[2]) :
#   print('Yes')
# else :
#   print('No')

#C
import math
n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
list_L, list_R = map(list, zip(*lr))
idx = list(range(n))
idx.sort(key=lambda x: list_L[x])

ans = []
current_sum = 0
for i in range(n) :
  if list_L[i] * list_R[i] > 0 :
    if current_sum > 0 :
      current_sum += list_L[i]
      ans.append(list_L[i])
    else :
      current_sum += list_R[i]
      ans.append(list_R[i])
  else :
    if current_sum > 0 :
      ans.append(max(-current_sum, list_L[i]))
      current_sum += ans[-1]
    elif current_sum < 0 :
      ans.append(min(-current_sum, list_R[i]))
      current_sum += ans[-1]
    else :
      ans.append(0)
if current_sum != 0 :
  print('No')
else :
  print(' '.join(map(str, ans)))
