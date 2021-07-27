def isPelindrome(st):
    if st == st[::-1]:
        return True

def solution(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i+1, n+1):
            tmp = s[i:j]
            if isPelindrome(tmp):
                if len(tmp) > res:
                    res = len(tmp)
    return res





print(solution("abcdcba"))
print(solution("abacde"))
print(solution("abacd"))