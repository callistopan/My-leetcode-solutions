class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]: 
        wordDict=Counter(wordDict)   
        res=[]
        t= self.dfs(s,wordDict,[],res)
        return res
       
    
    def dfs(self,s,wordDict,path,res):
        if len(s)==0:
            string = ' '.join(path)
            res.append(string)
            return 
        
        
        
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                self.dfs(s[i:],wordDict,path+[s[:i]],res)
               
'''
 Time complexity : O(2^n⋅n)   dictionary checking O(n)  and 
 
 If we assume the worst-case scenario where every possible partition needs to be checked, the number of partitions of a string of length n is 2^(n-1). This exponential growth is due to the fact that at each position, there is a choice to split or not split the string.


Space complexity :  O(2^n⋅n) 

The space complexity of the wordBreak function is dominated by the space required to store all possible sentences in the result list. Therefore, the overall space complexity is:

 O(2^n⋅n) 

'''