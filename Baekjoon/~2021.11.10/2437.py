import sys

input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
w.sort()
target = 1
for i in range(n):
    if target < w[i]:
        break
    target += w[i]
print(target)
