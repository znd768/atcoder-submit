# a, b = map(int, input().split())
# if a == b :
#   print(-1)
# else :
#   l = [1, 2, 3]
#   l.remove(a)
#   l.remove(b)
#   print(l.pop())

#ビンゴ判定
# n, m = map(int, input().split())
# al = list(map(int, input().split()))
# bl = list(map(int, input().split()))
# cl = sorted(al + bl)
# ans = 'No'
# for i in range(len(cl) - 1) :
#   if cl[i] in al and cl[i+1] in al :
#     ans = 'Yes'
# print(ans)

# n, t = map(int, input().split())
# al = list(map(lambda x: int(x) - 1, input().split()))
# ans = 0
# x = [False for _ in range(n**2)]
# row = [0 for _ in range(n)]
# col = [0 for _ in range(n)]
# diagonal = [0, 0]
# for i in range(t) :
#   x = al[i] // n
#   y = al[i] % n
#   row[x] += 1
#   if row[x] == n :
#     print(i+1)
#     exit()
#   col[y] += 1
#   if col[y] == n :
#     print(i+1)
#     exit()
#   if x == y :
#     diagonal[0] += 1
#     if diagonal[0] == n :
#       print(i + 1)
#       exit()
#   if x + y == n - 1 :
#     diagonal[1] += 1
#     if diagonal[1] == n :
#       print(i + 1)
#       exit()
#   pass
# print(-1)