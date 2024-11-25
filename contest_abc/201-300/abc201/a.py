x, y, z = map(int, input().split())
if (x+y) // 2 == z or (y+z) // 2 == x or (z+x) // 2 == y:
  print("Yes")
else:
  print("No")