n = int(input())
num_digits = len(str(n))
print(n if num_digits < 4 else n // 10**(num_digits - 3) * 10**(num_digits - 3))