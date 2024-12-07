n = int(input())
tv = [list(map(int, input().split())) for _ in range(n)]
current_qty = 0
prev_time = 0
for time, qty in tv:
    current_qty = max(0, current_qty - (time - prev_time)*1)
    prev_time = time
    current_qty += qty
    # print(f"{time = } {current_qty = }")
print(current_qty)