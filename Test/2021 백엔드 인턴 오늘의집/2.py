# 다리 건너기

n = int(input())

start = []
for i in range(n):
    start.append(int(input()))
end = []
tot = 0


def crossBridge(start, end):
    global tot
    if len(start) < 4:
        if len(start) == 3:
            # 가장 빠른 2명 보내기
            start.sort()
            tot += start[1]
            end += start[:2]
            start = start[2:]
            # 가장 빠른 한명 돌아오기
            tmp = end.pop(end.index(min(end)))
            tot += tmp
            start.insert(0, tmp)
            # 남은 2명 보내기
            tot += start[1]

        elif (len(start) == 2):
            # 2명 보내기
            tot += start[1]
        print(tot)

    else:
        # 가장 빠른 2명 보내기
        start.sort()
        tot += start[1]
        end += start[:2]
        start = start[2:]
        # 가장 빠른 1명 돌아오기
        tmp = end.pop(end.index(min(end)))
        tot += tmp
        start.insert(0, tmp)

        # 가장 느린 2명 보내기
        tot += start[-1]
        end += start[-2:]
        start = start[:-2]
        # end에서 가장 빠른 1명 복귀
        tmp = end.pop(end.index(min(end)))
        tot += tmp
        start.insert(1, tmp)
        # 반복
        crossBridge(start, end)


crossBridge(start, end)












