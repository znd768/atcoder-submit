# s, t = input().split()
# print('Yes') if s == 'AtCoder' and t == 'Land' else print('No')

# n, a = map(int, input().split())
# tl = list(map(int, input().split()))
# cur = 0
# for i in range(n) :
#   if cur >= tl[i] :
#     cur += a
#   else : cur = a + tl[i]
#   print(cur)

# import itertools
# n, m = map(int, input().split())
# sl = [input() for _ in range(n)]
# # ans = n
# for i in range(1, n + 1) :
#   c = itertools.combinations(range(n), i)
#   for e in c :
#     co = [0]*m
#     for shop_num in list(e) :
#       # print(list(e))
#       for j, s in enumerate(sl[shop_num]) :
#         if s == 'o' :
#           co[j] = 1
#     if co.count(0) == 0 :
#       print(i)
#       exit()

# n, m = map(int, input().split())
# al = list(map(int, input().split())) #個数、価格
# bl = list(map(int, input().split())) #個数の各条件
# al.sort()
# bl.sort()
# ans = 0
# cursor = 0
# for i in range(m) :
#   while cursor < n and al[cursor] < bl[i] :
#     cursor += 1
#   if i != m and cursor == n :
#     print(-1)
#     exit()
#   ans += al[cursor]
#   cursor += 1
# print(ans)

div = 998244353
k = int(input()) #k以下の文字列
cl = list(map(int, input().split())) #各文字についてこれより含んでたらアウト
n = 26
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for i in range(n) :
  old = []