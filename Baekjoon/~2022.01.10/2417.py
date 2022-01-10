import sys

input = sys.stdin.readline

n = int(input())
lt, rt = 0, n

while True:
    mid = (lt + rt) // 2
    if rt < lt:
        break
    if mid ** 2 < n:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt + 1)
