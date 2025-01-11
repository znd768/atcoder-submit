query_num = int(input())
queries = [list(map(int, input().split())) for _ in range(query_num)]
states = {}
exists = 0

for query in queries:
    command = query[0]
    if command == 1:
        num = query[1]
        if states.get(num, 0) == 0:
            states[num] = 0
            exists += 1
        states[num] += 1
    elif command == 2:
        num = query[1]
        states[num] -= 1
        if states[num] == 0:
            exists -= 1
            del states[num]
    elif command == 3:
        print(exists)