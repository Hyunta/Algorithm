import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
seq_command = deque(map(int, input().split()))

seq_after = deque(i for i in range(1, n + 1))
seq_before = deque()
while seq_command:
    command = seq_command.pop()
    tmp = seq_after.popleft()

    if command == 1:
        seq_before.appendleft(tmp)
    elif command == 2:
        seq_before.insert(1, tmp)
    elif command == 3:
        seq_before.append(tmp)

print(*seq_before)