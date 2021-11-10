import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    score = []
    fail = []
    for _ in range(n):
        score.append(list(map(int, input().split())))
    score.sort(key=lambda x: x[0])
    cnt = 1
    best = score[0][1]

    for i in range(1,n):
        if score[i][1] < best:
            best = score[i][1]
            cnt += 1
    print(cnt)
