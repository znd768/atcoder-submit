n = int(input())
s = input()
q = int(input())
cd = [tuple(input().split()) for _ in range(q)]
alphabets: str = "".join([chr(i+ord("a")) for i in range(26)])

def to_num(c: str) -> int:
    return ord(c) - ord('a')

for prev_char, next_char in cd:
    alphabets = alphabets.replace(prev_char, next_char)

ans = ""
for c in s:
    ans += alphabets[to_num(c)]
print(ans)