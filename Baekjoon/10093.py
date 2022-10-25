import sys

input = sys.stdin.readline

a, b = map(int, input().split())

res = a - b
if res < 0:
    res *= -1
elif res == 0:
    res += 1

print(res - 1)
c = min(a, b)
for i in range(1, res):
    print(c + i, end=" ")
