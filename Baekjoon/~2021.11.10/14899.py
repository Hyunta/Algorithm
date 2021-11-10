import sys
input = sys.stdin.readline

n = int(input())
member = [list(map(int, input().split())) for _ in range(n)]
pick = [False for _ in range(n)]
res = sys.maxsize


def Dfs(l, cnt):
    global res
    if l >= n:
        return
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if pick[i] and pick[j]:
                    start += member[i][j]
                elif not pick[i] and not pick[j]:
                    link += member[i][j]
        res = min(res, abs(start-link))

    else:
        pick[l] = True
        Dfs(l+1,cnt+1)
        pick[l] = False
        Dfs(l+1, cnt)


Dfs(0,0)
print(res)


