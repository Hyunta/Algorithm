from itertools import combinations

l = int(input())
s = [0] + list(map(int, input().split()))
n = int(input())

s.sort()
m = 0
if n in s:
    print(0)
else:
    for i in range(l):
        if s[i] < n < s[i + 1]:
            m = i

    cnt = 0
    if m < l - 1:
        case = [k for k in list(combinations([j for j in range(s[m] + 1, s[m + 1])], 2)) if k[0] <= n <= k[1]]

    else:
        case = [k for k in list(combinations([j for j in range(s[m] + 1, s[m + 1])], 2)) if k[0] <= n <= k[1]]
    print(len(case))
