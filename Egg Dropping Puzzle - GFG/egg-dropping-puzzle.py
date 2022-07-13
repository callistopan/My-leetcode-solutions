#User function Template for python3
INT_MAX = 32767
class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,eggs, floors):
        # code here
        
        eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
 
        # We need one trial for one floor and0 trials for 0 floors
        for i in range(1, n + 1):
            eggFloor[i][1] = 1
            eggFloor[i][0] = 0
     
        # We always need j trials for one egg and j floors.
        for j in range(1, k + 1):
            eggFloor[1][j] = j
     
        # Fill rest of the entries in table using optimal substructure
        # property
        for i in range(2, n + 1):
            for j in range(2, k + 1):
                eggFloor[i][j] = INT_MAX
                for x in range(1, j + 1):
                    res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                    if res < eggFloor[i][j]:
                        eggFloor[i][j] = res
     
        # eggFloor[n][k] holds the result
        return eggFloor[n][k]
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends