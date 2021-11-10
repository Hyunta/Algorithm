import sys

input = sys.stdin.readline


def make_pi(word):
    pi = [0] * len(word)
    j = 0
    for i in range(1, len(word)):
        while j > 0 and word[i] != word[j]:
            j = pi[j - 1]

        if word[i] == word[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(sentence, word, pi):
    result = []
    cnt = 0
    j = 0

    for i in range(len(sentence)):
        while j > 0 and sentence[i] != word[j]:
            j = pi[j - 1]

        if sentence[i] == word[j]:
            if j == (len(p) - 1):
                result.append(i - len(p) + 2)
                cnt += 1
                j = pi[j]
            else:
                j += 1
    print(cnt)
    for x in result:
        print(x)


t = input().rstrip()
p = input().rstrip()

kmp(t, p, make_pi(p))
