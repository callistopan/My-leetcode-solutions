class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=Counter(ransomNote)
        
        for i in magazine:
            if i in d:
                if d[i]!=0:
                    d[i]-=1
        for val in d.values():
            if val!=0:
                return False
            
        return True
