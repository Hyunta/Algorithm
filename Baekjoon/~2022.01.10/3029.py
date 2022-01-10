import sys

input = sys.stdin.readline


def calculate_time(hour, minute, second):
    return hour * 60 * 60 + minute * 60 + second


h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = calculate_time(h1, m1, s1)
t2 = calculate_time(h2, m2, s2)

t = t2 - t1 if t2 > t1 else t2 - t1 + 24 * 60 * 60
h = t // 60 // 60
m = t // 60 % 60
s = t % 60
print("%02d:%02d:%02d" % (h, m, s))
