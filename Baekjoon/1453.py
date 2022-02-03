import sys

input = sys.stdin.readline

n = int(input())
pc = [0] * 101
seats = list(map(int, input().split()))
cnt = 0
for seat in seats:
    if pc[seat] == 1:
        cnt += 1
    else:
        pc[seat] = 1
print(cnt)
