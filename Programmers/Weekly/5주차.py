cnt = 0
result = 0

def dfs(arr, word):
    global cnt
    global result
    order = ['A', 'E', 'I', 'O', 'U']
    if arr:
        cnt += 1
        if word == "".join(arr):
            result = cnt
            return
    if len(arr) == 5:
        return
    for alpha in order:
        arr.append(alpha)
        dfs(arr,word)
        arr.pop()

def solution(word):
    # answer = 0
    # dic = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    # arr = [781, 156, 31, 6, 1]
    # for idx,alpha in enumerate(word):
    #     answer += dic[alpha]*arr[idx] + 1
    # return answer
    dfs([], word)
    return result


print(solution("AAAAE"))
print(solution("A"))
print(solution("E"))
