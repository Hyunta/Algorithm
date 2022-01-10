import sys

input = sys.stdin.readline


def getLeast(word):
    answer = ""
    m = 0
    for i in range(len(word)):
        if word[i] == "M":
            m += 1
        elif word[i] == "K":
            if m:
                answer += str(10 ** m + 5)
            else:
                answer += "5"
            m = 0
    if m:
        answer += str(10 ** (m - 1))
    return answer


def getGreatest(word):
    answer = ""
    m = 0
    for i in range(len(word)):
        if word[i] == "M":
            m += 1
        elif word[i] == "K":
            if m:
                answer += str(5 * (10 ** m))
            else:
                answer += "5"
            m = 0
    if m:
        answer += "1" * m
    return answer

mk = input().rstrip()
print(getGreatest(mk))
print(getLeast(mk))