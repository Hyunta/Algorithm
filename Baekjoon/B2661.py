import sys
input = sys.stdin.readline


def check(num):
    length = len(num)
    for i in range(1, length//2 +1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    else:
        return True


def backTracking(num):
    global n
    if len(num) == n:
        print(num)
        exit()
    for i in "123":
        if check(num + str(i)):
            backTracking(num + str(i))
    return

n = int(input())
backTracking("1")

