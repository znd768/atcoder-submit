N = int(input())
T,A = 1,1
for _ in range(N):
  t,a = map(int, input().split())
  ma = max(-(-T//t),-(-A//a))
  T = t * ma
  A = a * ma
print(T + A)