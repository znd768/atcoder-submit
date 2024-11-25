n, a, b = map(int, input().split())
output1 = '.' * b
output2 = '#' * b
for j in range(n) :
  for _ in range(a) :
    for i in range(n) :
      if j & 1 :
        print(output1, end='') if i & 1 else print(output2, end='')
      else :
        print(output2, end='') if i & 1 else print(output1, end='')
    print()