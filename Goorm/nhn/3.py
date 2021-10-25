from itertools import permutations

conflict = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    conflict.append([a, b])
children = [i for i in range(1, 9)]
seq = list(permutations(children, 8))
cnt = 0
for s in seq:
    for con in conflict:
        a, b = con
        if str(str(a)+", "+str(b)) in str(s) or str(str(b)+", "+str(a)) in str(s):
            cnt += 1
            break
print(40320 - cnt)
