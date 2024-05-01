class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        number_of_eights = n//8
        reminder = n %8
        return (number_of_eights * (number_of_eights+1)//2)*8 + reminder*(number_of_eights + 1)
        
        
        
     