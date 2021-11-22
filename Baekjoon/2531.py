import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = list(int(input()) for _ in range(n))
lt, rt = 0, 0
answer = 0

while lt != n:
    rt = lt + k
    type_of_sushi = set()
    edible = True
    for i in range(lt, rt):
        type_of_sushi.add(sushi[i % n])
        if sushi[i % n] == c:
            edible = False
    cnt = len(type_of_sushi)
    if edible:
        cnt += 1
    answer = max(answer, cnt)
    lt += 1
print(answer)
