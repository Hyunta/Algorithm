import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dolls = list(map(int, input().split()))
answer = sys.maxsize
lion = []
for i in range(n):
    if dolls[i] == 1:
        lion.append(i)

lt = 0
rt = k - 1

if len(lion) < k:
    print(-1)
    exit(0)

while rt < len(lion):
    tmp = lion[rt] - lion[lt] + 1
    answer = min(answer, tmp)
    lt += 1
    rt += 1
print(answer)

