import sys

input = sys.stdin.readline
n = int(input())
price = []
for i in range(n):
    price.append(int(input()))
price.sort(reverse=True)

tot = 0
for i in range(n):
    if i % 3 == 2:
        continue
    else:
        tot += price[i]
print(tot)
