import sys

input = sys.stdin.readline
n = int(input())
machine = list(map(int, input().split()))
m = 0
machine.sort()

if len(machine) % 2 == 0:
    for i in range(n // 2):
        m = max(m, machine[i] + machine[n - 1 - i])
else:
    for i in range(n // 2):
        m = max(m, machine[i] + machine[n - 2 - i])
    m = max(m, machine[-1])
print(m)
