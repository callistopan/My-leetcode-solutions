class Solution:
    '''
    s = ((()
    ))(()
    ((()((
    if ( then ,if count <0 then set count as 0 and increase count in either case
    at the end if there is a positive count remaining then we need to add these much )s
    
    if ) then if count<0 then we need to increase move
    
    '''
    def minAddToMakeValid(self, s: str) -> int:
        
        if not s:
            return 0
        
        count=0
        moves=0
        
        for i in range(len(s)):
            
            if s[i]=='(':
                
                if count<0:
                    count=1
                else:
                    count+=1
                    
            else:
                count-=1
                if count<0:
                    moves+=1
                    
        if count>0:
            moves+=count
            
        return moves
        
        
        
        