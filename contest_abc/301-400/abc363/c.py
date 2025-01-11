import itertools

n, k = map(int, input().split())
s = input()
checked = set()
ans = 0

for x in itertools.permutations(s, n):
    p = "".join(x)
    if p in checked:
        continue
    checked.add(p)
    contain_palindrome = False
    for start in range(n - k + 1):
        sub_str = p[start:start+k]
        if sub_str == sub_str[::-1]:
            contain_palindrome = True
    if not contain_palindrome:
        ans += 1

print(ans)