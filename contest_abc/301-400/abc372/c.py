from bisect import bisect_left, insort_left
n, q = map(int, input().split())
s = input()
xc = [tuple(input().split()) for _ in range(q)]
current = s.count("ABC")
current_s = list(s)
for i, (x, c) in enumerate(xc):
    x = int(x) - 1
    left = max(0, x - 2)
    right = min(n - 1, x + 2)
    prev = "".join(current_s[left:right+1]).count("ABC")
    current_s[x] = c
    new = "".join(current_s[left:right+1]).count("ABC")
    if prev < new:
        current += 1
    elif prev > new:
        current -= 1
    print(current)