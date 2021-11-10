import sys

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li.sort(reverse=True)
res = []
for i in range(n):
    res.append(li[i] * (i+1))
print(max(res))
