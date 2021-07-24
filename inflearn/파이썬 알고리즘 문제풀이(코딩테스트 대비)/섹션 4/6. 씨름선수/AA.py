n = int(input())
M = [list(map(int, input().split())) for _ in range(n)]
M.sort(reverse=True)

heav=0
cnt=0
for h,w in M:
    if w >= heav:
        cnt+=1
        heav=w

print(cnt)

