import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
while n > 0:
    print(n)
    if n - 5 >= 0 and ((n - 5) % 2 == 0 or (n - 5) % 5 == 0):
        n -= 5
        cnt += 1
    else:
        n -= 2
        cnt += 1
if n < 0:
    print(-1)
else:
    print(cnt)
