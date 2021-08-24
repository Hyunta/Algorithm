import sys

input = sys.stdin.readline
n,s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

def DFS(l,tot):
    global cnt
    if l == n:
        if tot == s:
            cnt += 1
    else:
        DFS(l+1,tot+li[l])
        DFS(l+1,tot)

DFS(0,0)
if s ==0:
    cnt -= 1
print(cnt)
