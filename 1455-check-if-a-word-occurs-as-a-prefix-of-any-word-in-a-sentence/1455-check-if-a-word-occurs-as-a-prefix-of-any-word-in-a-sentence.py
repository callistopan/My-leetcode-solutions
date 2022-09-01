class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        
        for r,w in enumerate(words):
            
            n=len(w)
            m=len(searchWord)
            i=0
            j=0
            while i<n and j<m and w[i]==searchWord[j]:
                i+=1
                j+=1
                
            if j==m:
                return r+1
            
        return -1