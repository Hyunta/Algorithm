import sys

input = sys.stdin.readline

students = [False] * 30
for _ in range(28):
    num = int(input().rstrip()) - 1
    students[num] = True
for i in range(30):
    if not students[i]:
        print(i+1)
