class Solution:
    
    def __init__(self):
        
        self.valid_expressions =None
        self.min_removed =None
        
    def reset(self):
        
        self.valid_expressions = set()
        
        self.min_removed = float('inf')
        
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self.reset()
        
        self.remaining(s,0,0,0,[],0)
        
        return list(self.valid_expressions)
    
    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    
    def remaining(self,string,index,left,right,ans,ignored):
        
        if index == len(string):
            
            if left== right:
                
                if ignored <= self.min_removed: # we found an answer
                    
                    possible_ans =''.join(ans)
                    
                    if ignored < self.min_removed:
                        
                        self.valid_expressions = set()
                        
                        self.min_removed= ignored
                        
                    # add to our set
                    
                    self .valid_expressions.add(possible_ans)
                    
        else:
            
            char = string[index]
            
            if char not in '()':
                
                ans.append(char)
                
                self.remaining(string,index+1, left ,right, ans, ignored)
                
                ans.pop()
                
            else:
                
                # ignore the current char
                
                self.remaining(string,index+1,left,right,ans,ignored+1)
                
                # add current char
                
                ans.append(char)
                
                if string[index]=='(':
                    
                    self.remaining(string,index+1,left+1,right,ans,ignored)
                    
                elif right <left:
                    
                    self.remaining(string,index+1,left,right+1,ans,ignored)
                    
                ans.pop()
                    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    