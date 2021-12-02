import sys
input = sys.stdin.readline

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1:
        return False

    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result



n = int(input())
for _ in range(n):
    word = list(map(str, input().rstrip()))
    tmp = next_permutation(word)
    if tmp:
        print("".join(tmp))
    else:
        print("".join(word))

