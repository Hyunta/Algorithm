import sys

input = sys.stdin.readline


def dfs(len, idx):
    if len == l:
        vowel = 0
        conso = 0
        for i in range(l):
            if arr[i] in 'aeiou':
                vowel += 1
            else:
                conso += 1
        if vowel >= 1 and conso >= 2:
            print(''.join(arr))
        return
    for i in range(idx, c):
        if check[i] == 0:
            arr.append(s[i])
            check[i] = 1
            dfs(len + 1, i + 1)
            check[i] = 0
            del arr[-1]


l, c = map(int, input().split())
check = [0] * c
arr = []
s = input().split()
s.sort()
dfs(0, 0)
