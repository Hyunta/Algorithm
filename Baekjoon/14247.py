import sys

input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))
grows = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append((trees[i], grows[i]))

arr.sort(key=lambda x: (x[1]))
sum = 0
for i in range(n):
    sum += arr[i][0] + arr[i][1] * i

print(sum)