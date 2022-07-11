class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # take counter of first n elements in s_dict with n = len(p) - 1
        s_dict = collections.Counter(s[:len(p)-1]) 
        # counter of p, this should not be changed
        p_dict = collections.Counter(p)
        start = 0
        # final result list
        res = []
        # We iterate over the string s, and in each step we check if s_dict and p_dict match
        for i in range(len(p)-1, len(s)):
            # updating the counter & adding the character
            s_dict[s[i]] += 1
            # checking if counters match
            if s_dict == p_dict:
                res.append(start)
            # remove the first element from counter
            s_dict[s[start]] -= 1
            #if element count = 0, pop it from the counter
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            start += 1
            
        return res
        
#         res =[]
        
#         counter =Counter(p)
        
#         required = len(counter)
        
#         left,right,formed =0,0,0
        
#         d= {}
        
#         while right < len(s):
            
#             char = s[right]
            
#             d[char] = d.get(char,0)+1
            
#             if char in counter and d[char]== counter[char]:
                
#                 formed +=1
#             if right == len(s)-1 and formed== required:
#                 res.append(left)
#                 break
                
#             if right -left == len(p) -1  :
                
#                 if formed == required:

#                     res.append(left)
                
#                 d[s[left]]-=1
            
#                 if s[left] in counter and d[s[left]] < counter[s[left]]:
                
#                     formed -=1
                    
#                 left +=1
                
#             right+=1
       
            
#         return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            