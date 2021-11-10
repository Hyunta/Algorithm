from collections import deque
import sys

input = sys.stdin.readline

cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    val_list = list(map(int, input().split()))
    val_dict = dict()
    for x in val_list:
        val_dict[x] = val_dict.get(x,0) + 1
    q = deque((i,val_list[i]) for i in range(n))
    cnt = 0
    while True:
        tmp = q.popleft()
        if tmp[1] != max(val_dict.keys()):
            q.append(tmp)
        else:
            cnt += 1
            if tmp[0] == m:
                print(cnt)
                break
            if val_dict[tmp[1]] == 1:
                val_dict.pop(tmp[1])
            else:
                val_dict[tmp[1]] -= 1
