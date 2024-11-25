import math
w, h = map(int, input().split())
print(math.comb(w + h - 2, w - 1) % 1000000007)