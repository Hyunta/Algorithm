import sys

input = sys.stdin.readline

N, M = map(int, input().split())
py = input().rstrip()

while True:
    seq = 1
    for i in range(1, len(py)):
        if py[i] == py[i - 1]:
            seq += 1
        else:
            if seq >= M:
                py = py[:i - seq] + py[i:]
                break
            seq = 1
    else:
        if seq >= M:
            py = py[:len(py) - seq]
        break

if py:
    print(py)
else:
    print("CLEAR!")
