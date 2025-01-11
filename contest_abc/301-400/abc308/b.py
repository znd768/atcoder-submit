n, m = map(int, input().split())
strings = list(input().split())
d = list(input().split())
prices = list(map(int, input().split()))

basic_price = prices.pop(0)
name_price = {name: price for name, price in zip(d, prices)}
print(sum([name_price.get(name, basic_price) for name in strings]))