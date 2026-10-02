class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}
        for a in s:
            if a in '({[':
                stack.append(a)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != pairs[a]:
                    return False
        return len(stack) == 0