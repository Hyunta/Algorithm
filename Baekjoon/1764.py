import sys

input = sys.stdin.readline

n, m = map(int, input().split())
no_hear_set = set()
result = []

for i in range(n):
    no_hear_set.add(input().rstrip())

for i in range(m):
    tmp_name = input().rstrip()
    if tmp_name in no_hear_set:
        result.append(tmp_name)

result.sort()
print(len(result))
for x in result:
    print(x)
