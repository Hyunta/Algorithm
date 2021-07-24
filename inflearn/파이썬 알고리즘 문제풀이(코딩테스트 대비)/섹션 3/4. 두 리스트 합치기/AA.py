import sys
n = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))

res=[]
while n_li and m_li:
    if n_li[0] <= m_li[0]:
        res.append(n_li.pop(0))
    else:
        res.append(m_li.pop(0))

if n_li:
    res = res + n_li
else:
    res = res + m_li

for x in res:
    print(x, end=' ')