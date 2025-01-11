n, q = map(int, input().split())
el = [list(map(int, input().split())) for _ in range(q)]

d = dict.fromkeys(range(1, n+1), 0)

for command, num in el:
    match command:
        case 1:
            d[num] += 1
        case 2:
            d[num] += 2
        case 3:
            print("Yes" if d[num] >= 2 else "No")