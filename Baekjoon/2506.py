import sys

input = sys.stdin.readline

n = int(input())
test_result = list(map(int, input().split()))
current_score = 1
result = 0
for i in range(n):
    if test_result[i] == 1:
        result += current_score
        current_score += 1
    else:
        current_score = 1
print(result)
