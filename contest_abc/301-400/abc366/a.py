n, candidate_a, candidate_b = map(int, input().split())
rest = n - candidate_a - candidate_b
ans = True
if candidate_a == candidate_b:
    ans = False
elif candidate_b < candidate_a < candidate_b + rest:
    ans = False
elif candidate_a < candidate_b < candidate_a + rest:
    ans = False
print("Yes" if ans else "No")
