class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for x in s:
            if x in valid_map.values():
                if not stack:
                    return False
                last = stack.pop()
                if valid_map[last] is not x:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
