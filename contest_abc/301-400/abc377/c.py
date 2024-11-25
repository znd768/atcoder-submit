# rows number and cols number are n
# there are m knight chess pieces
# each knight chess piece is coordinate (x, y)
# i need to find the number of ways to put chess pieces on safe squares
n, m = map(int, input().split())
coordinate = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

def prevent_out_of_range(x, y, n):
  ret = []
  if x + 2 < n and y + 1 < n:
    ret.append((x + 2, y + 1))
  if x + 2 < n and y - 1 >= 0:
    ret.append((x + 2, y - 1))
  if x - 2 >= 0 and y + 1 < n:
    ret.append((x - 2, y + 1))
  if x - 2 >= 0 and y - 1 >= 0:
    ret.append((x - 2, y - 1))
  if x + 1 < n and y + 2 < n:
    ret.append((x + 1, y + 2))
  if x + 1 < n and y - 2 >= 0:
    ret.append((x + 1, y - 2))
  if x - 1 >= 0 and y + 2 < n:
    ret.append((x - 1, y + 2))
  if x - 1 >= 0 and y - 2 >= 0:
    ret.append((x - 1, y - 2))
  return ret

no = set()
for x, y in coordinate:
  no.add((x, y))
  for nx, ny in prevent_out_of_range(x, y, n):
    no.add((nx, ny))
print(n ** 2 - len(no))
