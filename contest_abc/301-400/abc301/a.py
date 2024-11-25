n = int(input())
s = input()
t_cnt = s.count('T')
a_cnt = n - t_cnt
if t_cnt == a_cnt:
  ans = 'T' if s[-1] == 'A' else 'A'
else:
  ans = 'T' if t_cnt > a_cnt else 'A'
print(ans)