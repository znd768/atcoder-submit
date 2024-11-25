# h = int(input())
# i = 0
# t = 0
# while h > t :
#   i += 1
#   t += 2 ** i
# print(i+1)

# n = int(input())
# nl = []
# ra = []
# for _ in range(n) :
#   s, t = input().split()
#   nl.append(s)
#   ra.append(int(t))
# sl = sorted(nl)
# print(sl[sum(ra)%n])

# import heapq
# n = int(input())
# powerl = []
# costl = []
# wl = [i for i in range(n)]
# for _ in range(n) :
#   a, c = map(int, input().split())
#   powerl.append(a)
#   costl.append(c)

# #カード番号リスト
# wl = sorted(wl, key=lambda x: costl[x])
# maxt = [powerl[wl[0]], costl[wl[0]]]
# keepl = [wl[0]]
# heapq.heapify(keepl)
# for i in range(n) :
#   if i == 0 : continue
#   if powerl[wl[i]] < maxt[0] and costl[wl[i]] > maxt[1]:
#     continue
#   else :
#     # keepl.append(wl[i])
#     heapq.heappush(keepl, wl[i])
#     maxt[0] = powerl[wl[i]]
#     maxt[1] = costl[wl[i]]

# #output
# c = len(keepl)
# print(c)
# ans = ''
# cnt = 0
# while True :
#   ans += str(heapq.heappop(keepl)+1)
#   cnt += 1
#   if cnt >= c : break
# print(*ans, sep=" ")

# n = int(input())
# powerl = []
# costl = []
# wl = [i for i in range(n)]
# for _ in range(n) :
#   a, c = map(int, input().split())
#   powerl.append(a)
#   costl.append(c)

# #カード番号リスト
# wl = sorted(wl, key=lambda x: costl[x])
# maxt = [powerl[wl[0]], costl[wl[0]]]
# keepl = [wl[0]]
# for i in range(n) :
#   if i == 0 : continue
#   if powerl[wl[i]] < maxt[0] and costl[wl[i]] > maxt[1]:
#     continue
#   else :
#     keepl.append(wl[i])
#     maxt[1] = costl[wl[i]]
#     maxt[0] = max(powerl[wl[i]], maxt[0])

# print(len(keepl))
# ans = ''
# for e in sorted(keepl) :
#   ans += str(e+1)+' '
# print(ans[:-1])

n = int(input())
al = []
bl = []
wl = [i for i in range(n)]
for _ in range(n) :
  a, c = map(int, input().split())
  al.append(a)
  bl.append(c)
a = 0
for i in range(n) :
  for j in range(i+1, n) :
    if al[i] == al[j] and bl[i] == bl[j] :
      a += 1
    elif al[i] == al[j] :
      a += 1
    elif bl[i] == bl[j] :
      a += 1
if not a & 1 :
  print('Takahashi')
else :
  print('Aoki')
print(a)
