class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        '''
        Sort the arrays.
        Traverse both array simultaneously and do following for every pair.
        If the difference is too small then, make it bigger by moving ‘a’ to a bigger value.
        If it is too big then, make it smaller by moving b to a bigger value.
        If it’s just right, return this pair.
        
        We are looking for two values, a and b, such that: 
        sumA - a + b = sumB - b + a
        2a - 2b  = sumA - sumB
        a - b  = (sumA - sumB) / 2
        
        '''
        
        a.sort()
        b.sort()
        
        sumA = sum(a)
        
        sumB = sum(b)
        
      
        
        i =0
        j =0
        
        while i < n and j <m:
            
            valA = sumA -a[i] + b[j]
            
            valB = sumB - b[j]+a[i]
            
            if valA== valB:
                
                return 1
                
            if valA> valB:
                
                i+=1
                
            else:
                
                j+=1
            
            
                
        return -1
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends