class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        '''
         generate all possible stirings and add to the queue if not seen 
         
         also note the smallest in each iteration
         
        '''
        q = deque()
        
        seen = {s}
        
        smallest =s
        
        q.append(s)
        
        
        while q:
            
            curr = q.popleft()
            
            if smallest > curr:
                
                smallest =curr
                
            add_a = list(curr)
            
            # add a to the odd positions 
            for i ,c in enumerate(add_a):
                
                if i %2==1:
                    
                    add_a[i] =str((int(c)+a)%10)
                    
            add_a =''.join(add_a)
            
            if add_a not in seen:
                
                seen.add(add_a)
                
                q.append(add_a)
             
            # rotate the array
            rotate=curr[-b:] + curr[:-b]
            
            if rotate not in seen:
                
                seen.add(rotate)
                
                q.append(rotate)
                
        return smallest
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    
            