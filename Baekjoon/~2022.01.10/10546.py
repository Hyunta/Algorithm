import sys

input = sys.stdin.readline

participants = dict()
n = int(input())
for _ in range(n):
    tmp = input().rstrip()
    participants[tmp] = participants.get(tmp, 0) + 1
for _ in range(n - 1):
    participants[input().rstrip()] -= 1
for k,v in participants.items():
    if v == 1:
        print(k)
        break
