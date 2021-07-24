n, k = map(int, input().split())
Q = []
for _ in range(n):
    Q.append(_+1)

cnt = 0

while len(Q) != 1:
    Q.append(Q.pop(0))
    cnt += 1
    if cnt%k == 0:
        Q.pop()
print(Q[0])
    


