import sys

input = sys.stdin.readline
n,k = map(int, input().split())
seq = [i for i in range(1,n+1)]


cnt = k-1
res = []
while seq:
    res.append(seq.pop(cnt))
    cnt += k-1
    if not seq:
        break
    print(cnt, len(seq))
    if cnt >= len(seq):
        cnt = cnt % len(seq)

answer ="<"
for i in range(len(res)):
    if i == len(res)-1:
        answer += str(res[i]) + ">"
        break
    answer += str(res[i]) + ", "

print(answer)


