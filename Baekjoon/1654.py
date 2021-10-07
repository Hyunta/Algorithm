import sys

input = sys.stdin.readline

k, n = map(int, input().split())
wires = []
for _ in range(k):
    wires.append(int(input()))
lt = 1
rt = max(wires)

while lt <= rt:
    mid = (lt + rt) // 2
    cut = 0
    for wire in wires:
        cut += wire // mid

    if cut >= n:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)
