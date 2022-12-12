import sys

input = sys.stdin.readline

n = int(input())

if n < 5:
    if n % 2 != 0:
        ans = -1
    else:
        ans = n // 2
else:
    q, r = divmod(n, 5)
    if r == 0:  # 5로 나누어 떨어지는 경우
        ans = q
    else:
        if r % 2 != 0:  # 5로 나누어 떨어지지 않지만 나머지가 1,3인 경우 -> 몫은 항상 1 이상이므로 하나 빼와서 6,8로 변경 가능
            q -= 1
            r += 5
        ans = q + r // 2
print(ans)
