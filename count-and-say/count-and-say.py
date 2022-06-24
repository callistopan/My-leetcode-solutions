class Solution:
    def countAndSay(self, n: int) -> str:
        ''' if n==1 then we just return "1"
            else just count and say of n-1 th term
            to calculate count and say just iterate over the string and               append the count and current integer in order'''
        if n==1:
            return "1"
        
        string=self.countAndSay(n-1)
        res=''
        count=1
        for i in range(1,len(string)):
            if string[i]!=string[i-1]:
                res+=str(count)+string[i-1]
                count=1
            else:
                count+=1
        res+=str(count)+string[-1]
        return res
            