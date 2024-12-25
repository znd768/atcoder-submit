num_of_house = int(input())
heights = list(map(int, input().split()))

ans = 1
for i in range(num_of_house - 1):
    for offset in range(i):
        prev = heights[offset]
        current = offset + i
        streak = 1
        while current < num_of_house:
            if prev == heights[current]:
                streak += 1
            else:
                ans = max(ans, streak)
                streak = 1
            prev = heights[current]
            current += i
        ans = max(ans, streak)
print(ans)