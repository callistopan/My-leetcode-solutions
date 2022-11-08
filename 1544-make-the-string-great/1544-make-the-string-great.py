class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack:
                if (s[i].isupper() and s[i].lower()==stack[-1]) or (s[i].islower() and s[i].upper()==stack[-1]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                
        return ''.join(stack)