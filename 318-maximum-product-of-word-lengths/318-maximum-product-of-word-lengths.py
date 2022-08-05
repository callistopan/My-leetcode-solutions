class Solution:
    def maxProduct(self, words: List[str]) -> int:
        '''
        
         make bit mask for each of the words and and them to check if they contain any duplicate elements
         
        
        '''
        n= len(words)
        
        bit_mask =[0]*n
        
        length =[0]*n
        
        for i in range(n):
            
            for c in words[i]:
                
                bit_mask[i]= bit_mask[i] | (1<<(ord(c)-ord('a')))   # set the curresponding bit of character
                
            length[i]= len(words[i])
            
        # and all the word bit_masks if it become zero then we are sure that there is no common letters
        
        
        max_len= float('-inf')
        for i in range(n):
            
            for j in range(i+1,n):
                
                if bit_mask[i] & bit_mask[j]==0 and length[i]*length[j] > max_len:
                    
                    max_len= length[i]*length[j]
                    
        return max_len if max_len!= float('-inf') else 0
            
            
        