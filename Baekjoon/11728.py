import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []

lt, rt = 0, 0
while True:
    if n <= lt:
        result += b[rt:]
        break
    elif m <= rt:
        result += a[lt:]
        break

    if a[lt] <= b[rt]:
        result.append(a[lt])
        lt += 1
    else:
        result.append(b[rt])
        rt += 1
print(*result)
