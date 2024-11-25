# n, m = map(int, input().split())
# hl = list(map(int, input().split()))
# ans = 0
# for e in hl :
#   m -= e
#   if m >= 0 :
#     ans += 1
# print(ans)

# s = input()
# sl = len(s)
# cn = 0
# for e in s :
#   if ord(e) >= 97 and ord(e) <= 122 :
#     cn += 1
# if cn <= sl // 2 :
#   print(s.upper())
# else : print(s.lower())

n = int(input())
basic = ['###', '#.#']
ans = ['' for _ in range(3**n)]
for i in range(3**n) :
  if (i - 1) % 3 == 0 :
    ans[i] += basic[1]*(3**n // 3)
  else :
    ans[i] += basic[0]*(3**n // 3)
for i in range(3**n // 3, 3**n - 3**n // 3) :
  ans[i] = ans[i][:3**n // 3] + '.'*3**(n-1) + ans[i][3**n - 3**n // 3:]

f = open('./output2.txt', 'w', encoding='utf-8')
for e in ans :
  f.writelines(e) 
  print(e)
f.close()
print('a')

# n = input()
# for i in range(int(n)) :
#   n += n
#   n = n[-1000000000000000:]

# print(int(n)%998244353)
# import sys
# sys.setrecursionlimit(10**6)
# n = int(input())
# al = list(map(lambda s : int(s)-1, input().split()))
# s = [0 for _ in range(n)]
# seen = [0 for _ in range(n)]
# def d(a) :
#   if seen[a] > 0 : return s[a]
#   seen[a] = 1
#   s[a] = 1
#   f = 1
#   f = max(f, d(al[a]) + 1)
#   s[a] = f
#   return s[a]
# ans = 0
# for i in range(n) :
#   ans += d(i)
#   print(ans)
#   print(s)
# print(ans)