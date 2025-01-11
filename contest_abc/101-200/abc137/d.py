from bisect import insort

job_num, days = map(int, input().split())
jobs = [tuple(map(int, input().split())) for _ in range(job_num)]
day_val = [[] for _ in range(10**5)]
for taken_day, val in jobs:
    day_val[taken_day-1].append(val)
reward = 0
candidates = []
for i in range(days):
    if len(day_val[i]) > 0:
        for val in day_val[i]:
            insort(candidates, val)
    if not candidates:
        continue
    reward += candidates[-1]
    del candidates[-1]

print(reward)