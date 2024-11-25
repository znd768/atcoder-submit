n = int(input())
d = dict()
ans = []
maxnum = 0
for _ in range(n) :
  s = input()
  if s in d :
    d[s] += 1
  else :
    d[s] = 1

l = sorted(d.items(), key=lambda t: t[1])
#最大値
ref = l[-1][1]

l = sorted(d.items(), key=lambda t: t[0])
print(l)

for a, b in l :
  if b == ref :
    print(a)