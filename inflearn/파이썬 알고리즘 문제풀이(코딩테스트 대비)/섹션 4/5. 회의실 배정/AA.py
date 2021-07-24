n = int(input())
M = [tuple(map(int, input().split())) for _ in range(n)]

M=sorted(M, key=lambda M:M[1])

cnt=0
e=0
for m in M:
    s=m[0]
    if s >= e:
        cnt += 1
        e = m[1]
print(cnt)
