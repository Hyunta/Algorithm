import sys

input = sys.stdin.readline
h, w = map(int, input().split())
block = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):
    lt = max(block[:i])
    rt = max(block[i + 1:])
    m = min(lt, rt)

    if m > block[i]:
        result += m - block[i]
print(result)