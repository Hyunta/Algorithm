import sys

input = sys.stdin.readline
n, m = map(int, input().split())
books = list(map(int, input().split()))

if n == 0:
    print(0)
    sys.exit(0)

box_cnt = 1
current_box = 0
for book in books:
    if current_box + book > m:
        box_cnt += 1
        current_box = 0
    current_box += book

print(box_cnt)
