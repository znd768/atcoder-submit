k = int(input())
s = input()
t = input()
sn = len(s)
tn = len(t)
if abs(sn-tn) > 1:
    print("No")
    exit()

ans = True
used_joker = False
for idx in range(min(sn, tn)):
    if s[idx] == t[idx]:
        continue
    elif not used_joker:
        used_joker = True
        if sn == tn:
            continue
        else:
            if sn > tn:
                t = "@" + t
            else:
                s = "@" + s
    else:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")


