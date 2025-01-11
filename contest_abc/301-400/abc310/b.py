n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(reverse=True, key=lambda x: x[0])

def check(num, lis):
    return num in lis

for j in range(n):
    for i in range(j+1, n):
        current = l[j]
        compare_target = l[i]
        is_same_price = current[0] == compare_target[0]
        have_same_func = all(map(lambda x: check(x, compare_target[2:]), current[2:]))
        if not is_same_price and have_same_func:
            print("Yes")
            exit()
        if is_same_price and have_same_func:
            if any(map(lambda x: not (check(x, current[2:])), compare_target[2:])):
                print("Yes")
                exit()
print("No")