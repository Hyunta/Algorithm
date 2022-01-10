import sys

input = sys.stdin.readline

frame_cnt = int(input())
total_cnt = int(input())
votes = list(map(int, input().split()))
frame = {}

cnt = 0
for vote in votes:
    print(frame)
    if len(frame) >= frame_cnt and vote not in frame:
        del frame[min(frame, key=lambda x: frame[x])]

    try:
        frame[vote][0] += 1
    except:
        frame[vote] = [1, cnt]
        cnt += 1

print(*sorted(frame.keys()))
