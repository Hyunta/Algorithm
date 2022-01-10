import sys

input = sys.stdin.readline
# 남학생 배수 변경
# 여학생 뽑은 번호 기준으로 좌우 대칭이면서 가장 많인 스위치 구간을 찾아서 모두 변경

totalSwitch = int(input())
switch = list(map(int, input().split()))
for _ in range(int(input())):
    gender, target = map(int, input().split())
    if gender == 1:  # 남자
        for i in range(totalSwitch):
            if (i + 1) % target == 0:
                switch[i] = switch[i] * (-1) + 1
    else:  # 여자
        target -= 1
        switch[target] = switch[target] * (-1) + 1
        lt, rt = target - 1, target + 1
        while True:
            if lt < 0 or rt > totalSwitch - 1:
                break
            if switch[lt] == switch[rt]:
                switch[lt] = switch[lt] * (-1) + 1
                switch[rt] = switch[rt] * (-1) + 1
            else:
                break
            lt -= 1
            rt += 1

for i in range(totalSwitch):
    print(switch[i], end=" ")
    if (i+1) % 20 == 0:
        print()
