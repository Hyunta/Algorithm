def count_words(s):
    cnt = 1
    res = []
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            res.append(cnt)
            cnt = 1
    if s[-1] == s[-2]:
        res.append(cnt + 1)
    else:
        res.append(cnt)
        res.append(1)
    res.sort()
    return res


def conn(s):
    while True:
        if s[0] != s[-1]:
            break
        s = s[-1] + s[:-1]
    return s


def solution(s):
    if s[0] != s[-1]:
        return count_words(s)
    elif len(set(s)) == 1:
        return [len(s)]
    else:
        s = conn(s)
        return count_words(s)


print(solution("aaabbaaa"))
print(solution("wowwow"))
print(solution("aaaaaa"))
