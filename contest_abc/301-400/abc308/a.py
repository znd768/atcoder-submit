sl = list(map(int, input().split()))
def check(num):
    return num % 25 == 0
def check2(num):
    return 100 <= num <= 675
if all(map(check, sl)) and all(map(check2, sl)) and sorted(sl) == sl:
    print("Yes")
else:
    print("No")