from collections import defaultdict
scores = list(map(int, input().split()))
contenders = ["A", "B", "C", "D", "E"]
result = defaultdict(list)
for bit in range(1 << 5):
    score = 0
    name = ""
    for i in range(5):
        if bit & (1 << i):
            score += scores[i]
            name += contenders[i]
    result[score].append(name)
for score, names in sorted(result.items(), reverse=True):
    for name in sorted(names):
        print(name)