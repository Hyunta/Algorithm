import sys

input = sys.stdin.readline
pos = []
neg = []
res = 0
for _ in range(int(input())):
    n = int(input())
    if n > 1:
        pos.append(n)
    elif n == 1:
        res += 1
    else:
        neg.append(n)

pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        res += pos[i] * pos[i + 1]
else:
    for i in range(0, len(pos) - 1, 2):
        res += pos[i] * pos[i + 1]
    res += pos[-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        res += neg[i] * neg[i + 1]
else:
    for i in range(0, len(neg) - 1, 2):
        res += neg[i] * neg[i + 1]
    res += neg[-1]


print(res)
