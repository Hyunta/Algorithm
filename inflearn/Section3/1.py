'''
회문 문자열 검사
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)
이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''

N = int(input())

for n in range(N):
    M = input()
    m = M.lower()
    if m[::-1] == m:
        print("#%d"%(n+1),"YES")
    else:
        print("#%d"%(n+1),"NO") 