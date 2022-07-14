#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        
        chars =[0]*26
        
        # make all chars of A as 1
        
        for c in A:
            
            chars[ord(c)-ord('a')]=1
            
        # now traverse the second array and if it is already present in chars then mark it -1
        # if not present in chars then make it 2
        
        for c in B:
            
            if chars[ord(c)-ord('a')] ==1 or chars[ord(c)-ord('a')] ==-1:
                
                chars[ord(c)-ord('a')]=-1
                
            if chars[ord(c)-ord('a')]==0:
                
                chars[ord(c)-ord('a')]=2
                
        # again traverse the chars 
        
        res=''
        
        for i in range(26):
            
            if chars[i]==2 or chars[i]==1:
                
                res+=chr(i+ord('a'))
                
        return res if res else "-1"
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends