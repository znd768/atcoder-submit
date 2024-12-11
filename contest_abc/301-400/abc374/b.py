s = input()
t = input()
if s == t:
    print(0)
else:
    for i, (char1, char2) in enumerate(zip(s, t), start=1):
        if char1 != char2:
            print(i)
            exit()
    else:
        print(min(len(s), len(t)) + 1)