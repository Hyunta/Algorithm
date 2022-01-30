import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

com = []
for i in range(1, n + 1):
    com.append(list(combinations(arr, i)))

answer = 1000000000
for combined in com:
    for each in combined:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        answer = min(answer, abs(sour - bitter))

print(answer)
