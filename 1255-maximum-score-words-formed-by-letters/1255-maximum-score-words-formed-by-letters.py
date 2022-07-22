class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if not words or not letters or not score:
            return 0
        
        count=[0]*26
        
        for letter in letters:
            count[ord(letter)-ord('a')]+=1
        
        res = self.backtrack(words,count,score,0)
        
        return res
    
    def backtrack(self,words,count,score,index):
        
        max_score =0
        
        for i in range(index,len(words)):
            
            res =0
            
            isValid=True
            
            for char in words[i]:
                
                count[ord(char)-ord('a')]-=1
                
                res += score[ord(char)-ord('a')]
                
                if count[ord(char)-ord('a')] <0:
                    isValid=False
                    
            if isValid:
                res+=self.backtrack(words,count,score,i+1)
                max_score=max(max_score,res)
                
                
            # not valid or we are removing this word
            
            for char in words[i]:
                count[ord(char)-ord('a')]+=1
                res=0
                
                
        return max_score