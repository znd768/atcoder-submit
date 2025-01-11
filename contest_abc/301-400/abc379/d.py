from collections import deque
query_num = int(input())
queries = [list(input().split()) for _ in range(query_num)]

d = deque()
today = 0

for query in queries:
  if query[0] == '1':
    d.append(today)
  elif query[0] == '2':
    today += int(query[1])
  else:
    cnt = 0
    flg = True
    while d and flg:
      p = d.popleft()
      if today - p < int(query[1]):
        d.appendleft(p)
        flg = False
      if flg:
        cnt += 1
    print(cnt)
  