import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
li = []
for key, val in enumerate(nums):
    li.append([val, key])
li.sort()
res = [0] * n
for i, tmp in enumerate(li):
    a, b = tmp
    res[b] = i
print(*res)
