#import sys
#sys.stdin=open("input.txt","rt")

# N K / (1<= N <= 10000, 1<=K<=N)

N,K = map(int, input().split())

M=[]
for n in range(1, N+1):
    if N%n == 0:
        M.append(n)


if K > len(M):
    print(-1)
else:
    print(M[K-1])
