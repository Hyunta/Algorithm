import sys
input = sys.stdin.readline

eq = input().rstrip().split('-')
values = []
for val in eq:
    tmp = val.split('+')
    tot = 0
    for x in tmp:
        tot += int(x)
    if values:
        values.append(-tot)
    else:
        values.append(tot)
print(sum(values))



