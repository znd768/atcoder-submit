n, m, d = map(int, input().split())
a_l = list(map(int, input().split()))
b_l = list(map(int, input().split()))
a_l.sort()
b_l.sort()
ans = -1
cursor_a = 0
cursor_b = 0
while cursor_a < n and cursor_b < m:
    if abs(a_l[cursor_a] - b_l[cursor_b]) <= d:
        ans = max(ans, a_l[cursor_a] + b_l[cursor_b])
        if cursor_a + 1 < n and cursor_b + 1 < m:
            if a_l[cursor_a + 1] < b_l[cursor_b + 1]:
                cursor_a += 1
            else:
                cursor_b += 1
        elif cursor_a + 1 < n:
            cursor_a += 1
        else:
            cursor_b += 1
    elif a_l[cursor_a] < b_l[cursor_b]:
        cursor_a += 1
    else:
        cursor_b += 1
print(ans)