class Solution:
    def waysToReachStair(self, k: int) -> int:
        self.memo = {}
        self.power = [0]*33
        for i in range(33):
            self.power[i] = pow(2,i)
        return self.dfs(1,1,0,0,k)
    
    def dfs(self, pos, stat, jump, back, k):
        if pos > k + 1:
            return 0
        if (jump,back,stat) in self.memo:
            return self.memo[(jump,back,stat)]
        ans = 0
        
        if pos == k:
            ans+=1
        
        if stat == 1: # going back a step is possible
            ans += self.dfs(pos-1, 0, jump, back +1,k)
            ans += self.dfs(pos+self.power[jump],1,jump+1,back,k)
        if stat == 0: # no going back
            ans += self.dfs(pos+self.power[jump],1,jump+1,back,k)
        self.memo[(jump,back,stat)] = ans
        return ans
            
        
'''Funtion used for the recursion will have the following parameters

pos - step number
stat - indicates whether backstep is allowed
jump - number of forward jumps performed
back - number of backsteps

We get a unique state using the parameters jump, back and stat.

jump and back parameter will not exceed 40 as max value of k is 10^9( 2^40 >>> 10^9)
stat will have two value. (0-when backstep is not allowed, 1-when backstep is allowed)

So we can use a memo of the form dp[50][50][2].'''