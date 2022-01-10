import sys

input = sys.stdin.readline

n = int(input())
color = list(input().rstrip())
start = color[0]
changeB = 'B'
changeR = 'R'
count = [1] * 3

for c in color:
    if start != c:
        count[0] += 1
        start = c
    if c == 'R':
        if changeB == 'B':
            count[1] += 1
            changeB = 'R'
        changeR = 'R'
    elif c == 'B':
        if changeR == 'R':
            count[2] += 1
            changeR = 'B'
        changeB = 'B'
print(min(count))

