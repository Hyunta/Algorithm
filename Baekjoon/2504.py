import sys

input = sys.stdin.readline


def check(string):
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        elif not stack:
            return False
        else:
            tmp = stack.pop()
            if (tmp == '[' and x == ')') or (tmp == '(' and x == ']'):
                return False
    return True


def calculate(string):
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        else:
            tmp = stack.pop()
            if x == ')':
                if tmp == '(':
                    stack.append(2)
                else:
                    tmp_val = tmp
                    while True:
                        val = stack.pop()
                        if val == '(':
                            stack.append(tmp_val * 2)
                            break
                        else:
                            tmp_val += val
            else:
                if tmp == '[':
                    stack.append(3)
                else:
                    tmp_val = tmp
                    while True:
                        val = stack.pop()
                        if val == '[':
                            stack.append(tmp_val * 3)
                            break
                        else:
                            tmp_val += val
    return sum(stack)


if __name__ == "__main__":
    p = list(map(str, input().rstrip()))
    stack = []
    res = 0

    if check(p):
        print(calculate(p))
    else:
        print(0)
