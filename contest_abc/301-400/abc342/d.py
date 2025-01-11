from collections import Counter

def prime_factorization(n) :
    i = 2
    factors = []
    while i * i <= n :
        if n % i :
            i += 1
        else :
            n //= i
            factors.append(i)
    if n > 1 :
        factors.append(n)
    return factors

n = int(input())
al = list(map(int, input().split()))
root = []

for num in al:
    if num == 0:
        root.append(0)
        continue
    c = Counter(prime_factorization(num))
    tmp = 1
    for k, v in c.items() :
        if v & 1:
            tmp *= k
    root.append(tmp)

ans = 0
c = Counter(root)
for k, v in c.items():
    if k == 0:
        for i in range(1, v+1):
            ans += n - i
    else:
        ans += v*(v-1)//2
print(ans)