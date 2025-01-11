h, w = map(int, input().split())
l = [input() for _ in range(h)]
moves_h = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
moves_w = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
target_str = "snuke"
for i in range(h):
    for j in range(w):
        for dh, dw in zip(moves_h, moves_w):
            for c in range(5):
                if i+dh*c < 0 or i+dh*c >= h or j+dw*c < 0 or j+dw*c >= w:
                    break
                if l[i+dh*c][j+dw*c] != target_str[c]:
                    break
                if c == 4:
                    # found
                    for k in range(5):
                        print(i+dh*k+1, j+dw*k+1)