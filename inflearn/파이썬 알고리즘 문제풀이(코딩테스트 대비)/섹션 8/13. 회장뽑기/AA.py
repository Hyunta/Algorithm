n = int(input())
m = []
while True:
    x,y = map(int, input().split())
    if x == -1 and y == -1:
        break
    else:
        m.append([x,y])
dis = list([100]*n for _ in range(n))
for x in m:
    dis[x[0]-1][x[1]-1] = 1
    dis[x[1]-1][x[0]-1] = 1
for i in range(n):
    dis[i][i] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] + dis[k][j] < dis[i][j]:
                dis[i][j] = dis[i][k]+dis[k][j]
res = []
res2 = []
for x in dis:
    res.append(max(x))

for k,v in enumerate(res):
    if v == min(res):
        res2.append(k+1)
print(min(res), len(res2))
for x in res2:
    print(x, end=' ')
