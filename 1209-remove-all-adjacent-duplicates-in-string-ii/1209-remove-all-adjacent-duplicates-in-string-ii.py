class charNode:
    def __init__(self,char,count):
        self.char=char
        self.count=count
        
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        n=len(s)
        stack=[]
        
        for i in range(n):
            if not stack or stack[-1].char!= s[i]:
                node= charNode(s[i],1)
                stack.append(node)
                
                
            elif stack and stack[-1].char==s[i]:
                stack[-1].count+=1
                
                if stack[-1].count==k:
                    stack.pop()
                    
            
        return ''.join([node.char*node.count for node in stack])