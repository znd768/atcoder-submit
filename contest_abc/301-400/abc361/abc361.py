#a
# n, k, x = map(int, input().split())
# al = list(map(int, input().split()))

# al.insert(k, x)
# print(' '.join(map(str, al)))

#b
# al = list(map(int, input().split()))
# bl = list(map(int, input().split()))
# t1 = al[0] < bl[3] and bl[0] < al[3]
# t2 = al[1] < bl[4] and bl[1] < al[4]
# t3 = al[2] < bl[5] and bl[2] < al[5]
# # print(t1, t2, t3)
# ans = t1 and t2 and t3
# if ans :
#   print('Yes')
# else :
#   print('No')

#c
# n, k = map(int, input().split())
# al = sorted(list(map(int, input().split())))

# l = 0
# r = n - 1
# for i in range(k) :
#   if al[l + 1] - al[l] >= al[r] - al[r - 1] :
#     l += 1
#   else :
#     r -= 1
# print(al[r] - al[l])