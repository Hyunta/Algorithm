import sys

input = sys.stdin.readline


def check(words):
    for x in words:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')' or x == ']':
            if not stack:
                return 'no'
            tmp = stack.pop()
            if (tmp == '(' and x == ']') or (tmp == '[' and x == ')'):
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'


while True:
    para = list(map(str, input().rstrip()))
    stack = []
    if para[0] == '.':
        break
    print(check(para))

