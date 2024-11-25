# s = input()
# if s.index('R') < s.index('M') :
#   print('Yes')
# else :
#   print('No')

# s, t = input().split()
# ans = 'No'
# for i in range(1, len(s)) :
#   for c in range(i) :
#     m = ''
#     while c < len(s) :
#       m += s[c]
#       c += i
#     # print(m)
#     if m == t :
#       ans = 'Yes'
# print(ans)

# from collections import defaultdict
# n = int(input())
# al = list(map(int, input().split())) #箱の番号
# wl = list(map(int, input().split())) #各荷物の重さ
# d = defaultdict(lambda: [0, 0])
# s = 0
# for i, e in enumerate(al) :
#   if d[e][0] == 0 :
#     d[e] = [d[e][0] + 1, wl[i]]
#   elif d[e][1] > wl[i] :
#     s += wl[i]
#     d[e] = [d[e][0] + 1, d[e][1]]
#   else :
#     s += d[e][1]
#     d[e] = [d[e][0] + 1, wl[i]]
# print(s)

# import bisect
# n, t = map(int, input().split())
# s = input()
# xl = list(map(int, input().split()))
# idx = list(range(n))
# idx.sort(key=lambda x:xl[x])
# ans = 0
# al = []
# bl = []
# for i in range(n) :
#   if s[idx[i]] == '0' :
#     bl.append(xl[idx[i]])
#   else :
#     al.append(xl[idx[i]])
# for e in al :
#   left = bisect.bisect_left(bl, e)
#   right = bisect.bisect_right(bl, e + t*2)
#   ans += right - left
#   # print(e, left, right)
# print(ans)

# n, k = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
