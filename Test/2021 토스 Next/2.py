'''
문제 설명
나만의 L4 만들기
여러 대의 서버로 부하를 분산하는 로드밸런서를 만들고자 합니다. 해당 로드밸런서는 기본적으로는 라운드 로빈 방식으로 요청을 서버로 분배합니다. 다만 요청의 sticky 옵션이 true인 경우 이전에 분배된 서버로 요청이 분배되어야 합니다. 이러한 동작을 수행하는 함수를 구현해보세요.

라운드 로빈 방식 : 1번 서버부터 시작, 1, 2, ... N, 그리고 다시 1, 2, ... 순서입니다.
예시1
2개의 서버에 라운드 로빈 방식으로 요청을 분배한다면 아래와 같이 동작해야 합니다.

int servers = 2;
boolean sticky = false;
List requests = Arrays.asList(1,2,3,4);

List result = solution(servers, sticky, requests);

println(result); // [1,3], [2,4]
출력 결과인 [1,3], [2,4]가 의미하는 바는 1번 서버에 1번과 3번 요청이 전달되었으며, 2번 서버에 2번과 4번 요청이 전달되었다는 의미입니다.

예시2
2개의 서버에 sticky 옵션을 true로 요청한 경우에는 아래와 같이 동작해야 합니다.

int servers = 2;
boolean sticky = true;
List requests = Arrays.asList(1,1,2,2);

List result = solution(servers, sticky, requests);

println(result); // [1,1], [2,2]
출력 결과인 [1,1], [2,2]가 의미하는 바는 첫 번째 서버에 1번 요청이 2개 전달되었으며, 두 번째 서버에 2번 요청이 2개 전달되었다는 의미입니다.

예시3
약간 더 복잡한 사례를 살펴보겠습니다. 2개의 서버에 sticky 옵션을 true로 요청한 경우에는 아래와 같이 동작해야 합니다.

int servers = 2;
boolean sticky = true;
List requests = Arrays.asList(1,2,2,3,4,1);

List result = solution(servers, sticky, requests);

println(result); // [1,3,1], [2,2,4]
출력 결과인 [1,3,1], [2,2,4]가 의미하는 바는 첫 번째 서버에 1번, 3번, 1번 요청이 전달되었으며, 두 번째 서버에 2번, 2번, 4번 요청이 전달되었다는 의미입니다.
'''

def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    if sticky:
        cnt = 0
        for i in range(len(requests)):
            for j in range(len(answer)):
                if requests[i] in answer[j]:
                    answer[j].append(requests[i])
                    break
            else:
                answer[cnt].append(requests[i])
                cnt += 1
                if cnt >= servers:
                    cnt = cnt%servers
    else:
        for i in range(len(requests)):
            answer[i % servers].append(requests[i])
    print(answer)

print(solution(2,False,[1,2]))
print(solution(2,True,[1,1,2,2]))


