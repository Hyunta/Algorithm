n = int(input())
def DFS(x):
    if x > 0:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    DFS(n)