def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    isConn = {costs[0][0],costs[0][1]}
    ans = costs[0][2]
    while len(isConn) != n:
        for i,cost in enumerate(costs):
            if cost[0] in isConn and cost[1] in isConn:
                continue
            if cost[0] in isConn or cost[1] in isConn:
                ans += cost[2]
                isConn.update([cost[0],cost[1]])
                costs[i] = [-1,-1,-1]
                break
    return ans


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
print(solution(5, [[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]))