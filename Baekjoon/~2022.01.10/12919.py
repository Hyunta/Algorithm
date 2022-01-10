import sys


def dfs(word):
    if len(word) == len(s):
        if word == s:
            print(1)
            exit(0)
        return

    if word[0] == 'B':
        word = word[::-1]
        word.pop()
        dfs(word)
        word.append('B')
        word = word[::-1]

    if word[-1] == 'A':
        word.pop()
        dfs(word)
        word.append('A')


if __name__ == "__main__":
    input = sys.stdin.readline
    s = list(input().rstrip())
    t = list(input().rstrip())
    dfs(t)
    print(0)
