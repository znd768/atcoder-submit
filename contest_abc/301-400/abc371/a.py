s1, s2, s3 = input().split()
if s1 == s2 == s3:
  print('B')
elif s1 == s3 and s1 != s2 :
  print('B')
elif s1 != s2 and s2 == s3:
  print('A')
else :
  print('C')