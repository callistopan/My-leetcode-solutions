#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        
        activity =[]
        
        for i in range(n):
            
            activity.append([start[i]  , end[i]])
            
        activity.sort( key =  lambda x :x[1]) # sort by end time
        
        
        res =1
        
        j = 0 
        
        for i in range(n):
            
            if activity[i][0] > activity[j][1]:
                
                res+=1
                
                j =i
                
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends