import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = []
test = []
cnt = 0

for _ in range(n):
    s.append(input().rstrip())
for _ in range(m):
    tmp = input().rstrip()
    if tmp in s:
        cnt += 1
print(cnt)


