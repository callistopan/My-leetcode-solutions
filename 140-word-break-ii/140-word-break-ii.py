class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''both solution takes O(n) time'''
       
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
               
               