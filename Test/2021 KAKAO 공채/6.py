def solution(board, skill):

    for s in skill:
        print(s)
        type,x1,y1,x2,y2,deg = s
        if type == 1:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    board[i][j] -= deg
        else:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    board[i][j] += deg
    cnt=0
    for row in board:
        for x in row:
            if x >= 1:
                cnt +=1
    return cnt

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
