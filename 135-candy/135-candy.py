class Solution:
    def candy(self, ratings: List[int]) -> int:
        ''' travese from left to right 
            if the next child has greater rating then update his rating 
            then taraverse back and check if rating are satisfying the condition'''
        
        n=len(ratings)
        
        candies=[1]*n
        
        for i in range(n-1):
            
            if ratings[i+1]>ratings[i]:
                
                candies[i+1] = 1 + candies[i]
                
        # traverse in reverse order
        
        for i in range(n-2,-1,-1):
            
            if ratings[i] > ratings[i+1]:
                
                if candies[i] <= candies[i+1]:
                    
                    candies[i] = 1 + candies[i+1]
                    
                    
        return sum(candies)
                    
                    
            
        