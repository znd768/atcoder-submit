n, rating = map(int, input().split())
ad = [list(map(int, input().split())) for _ in range(n)]
current_rating = rating
for type_num, score in ad:
    if type_num == 1 and 1600 <= current_rating <= 2799:
        current_rating += score
    elif type_num == 2 and 1200 <= current_rating <= 2399:
        current_rating += score
print(current_rating)
