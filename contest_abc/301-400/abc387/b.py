x = int(input())
print(sum([i*j for i in range(1, 10) for j in range(1, 10) if i*j != x]))