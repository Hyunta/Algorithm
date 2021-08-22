def solution(infos, actions):
    login = False
    cart = []
    answer = []
    for action in actions:
        action_li = list(map(str, action.split()))
        print(action)
        if action_li[0] == "LOGIN":
            if action[6:] in infos and not login:
                login = True
                answer.append(True)
            else:
                answer.append(False)
        elif action_li[0] == "ADD":
            if login:
                cart.append(action_li[1])
                answer.append(True)
            else:
                answer.append(False)
        elif action_li[0] == "ORDER":
            if cart:
                cart = []
                answer.append(True)
            else:
                answer.append(False)
    return answer