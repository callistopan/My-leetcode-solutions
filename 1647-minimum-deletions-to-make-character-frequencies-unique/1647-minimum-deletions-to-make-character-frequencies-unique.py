class Solution:
    def minDeletions(self, s: str) -> int:
        frequency=[0]*26
        for char in s:
            frequency[ord(char)-ord('a')]+=1
        frequency.sort(reverse=True)
        delete_count=0
        
        max_freq_allowed=len(s) # maximum frequency allowed
        
        for freq in frequency:
            
            if freq >max_freq_allowed:
                delete_count+= freq - max_freq_allowed
                freq=max_freq_allowed
            
            max_freq_allowed=max(0,freq-1)
            
        return delete_count
        
        
        
        
        
        
        
        

        
    def minDeletion2(s):
        
        '''time complexity== O(N+K^2) K is the maximum possible number of distinct characters'''
        frequency=[0]*26
        for char in s:
            frequency[ord(char)-ord('a')]+=1
        delete_count=0
        seen_frequencies=set()
        
        for i in range(26):
            while frequency[i] and frequency[i] in seen_frequencies:
                frequency[i]-=1
                delete_count+=1
                
            seen_frequencies.add(frequency[i])
        return delete_count