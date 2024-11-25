#B
n = int(input())
al = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
current_value = 0
for i in range(n) :
  if current_value >= i :
    current_value = al[current_value][i]
  else :
    current_value = al[i][current_value]
print(current_value + 1)