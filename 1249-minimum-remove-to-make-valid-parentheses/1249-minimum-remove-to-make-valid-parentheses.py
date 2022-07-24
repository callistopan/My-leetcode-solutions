class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''   # remove this ')'
        while stack: # remove extra '('s
            s[stack.pop()] = ''
        return ''.join(s)  # join final string
            