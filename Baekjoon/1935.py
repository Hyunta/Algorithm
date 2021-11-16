import sys

input = sys.stdin.readline
n = int(input())
tmp = input().rstrip()
stack = []
nums = [int(input()) for _ in range(n)]


def calculate(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    elif operator == '*':
        return first * second
    elif operator == '/':
        return first / second


for x in tmp:
    if x.isalpha():
        stack.append(nums[ord(x) - ord('A')])

    else:
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(calculate(a, b, x))
print(f'{stack[0]:.2f}')
