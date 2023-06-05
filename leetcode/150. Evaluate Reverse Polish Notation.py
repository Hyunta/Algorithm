class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        PLUS, MINUS, MULTIPLY, DIVIDE = "+", "-", "*", "/"
        stack = []
        for token in tokens:
            if token.isnumeric() or len(token) > 1:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token is PLUS:
                    stack.append(first + second)
                elif token is MINUS:
                    stack.append(first - second)
                elif token is MULTIPLY:
                    stack.append(first * second)
                elif token is DIVIDE:
                    stack.append(int(first / second))
        return stack[-1]