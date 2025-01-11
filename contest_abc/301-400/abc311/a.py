n = int(input())
s = input()
abc = set(list("ABC"))
print(abc)
for i, chara in enumerate(s, start=1):
    abc |= {chara}
    print(abc)
    if len(abc) == 0:
        print(i)
        break