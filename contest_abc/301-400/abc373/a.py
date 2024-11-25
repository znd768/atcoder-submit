string_list = [input() for _ in range(12)]
print(sum([1 for i, e in enumerate(string_list, start=1) if i == len(e)]))