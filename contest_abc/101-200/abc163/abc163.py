import math
a, b, c = map(int, input().split())
if math.sqrt(a*b)*2 < c - a - b:
  print('Yes')
else : print('No')