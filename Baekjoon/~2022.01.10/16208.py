import sys

input = sys.stdin.readline
n = int(input())
demand_len = list(map(int, input().split()))
demand_len.sort()

tot_len = sum(demand_len)
cost = 0
for each_len in demand_len:
    tot_len -= each_len
    cost += each_len * tot_len
print(cost)