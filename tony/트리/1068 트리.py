import sys

DELETED = -2

input = sys.stdin.readline


def delete_node(num, arr):
    arr[num] = DELETED
    for i in range(len(arr)):
        if num == arr[i]:
            delete_node(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

delete_node(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)