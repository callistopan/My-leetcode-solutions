class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char=[0]*26
        
        for  i in sentence:
            char[ord(i)-ord('a')]+=1
        for i in range(26):
            if char[i]==0:
                return False
            
        return True