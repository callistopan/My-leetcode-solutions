class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        
        c = 0
        for m in message:
            if m in s:
                c +=1
            if c>=2:
                return True
        return False