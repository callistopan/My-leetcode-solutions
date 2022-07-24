class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        n=len(s)
        stack=[]
        
        for i in range(n):
            if not stack or stack[-1][0]!= s[i]:
                stack.append([s[i],1])
                
                
            elif stack and stack[-1][0]==s[i]:
                stack[-1][1]+=1
                
                if stack[-1][1]==k:
                    stack.pop()
                    
            
        return ''.join([char*count for char,count in stack])