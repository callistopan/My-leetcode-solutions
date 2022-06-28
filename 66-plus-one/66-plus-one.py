class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ''' traverse the array from end 
            if current number is less than 9 we can increase this particular element and return
            else make it 0 until we find an element less than 0
            if we are not returning in the loop then make an array of all zeros of size n+1 and 
            make first element as 1'''
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        newNumber=[0]*(n+1)
        newNumber[0]=1
        
        return newNumber
        
        
    '''elements of programming interview version'''
    
    def plus_one_epi(self,digits):
        digits[-1]+=1
        
        for i in reversed(range(1,len(A))):
            if digits[i] !=10:
                break
                
            digits[i]=0
            digits[i-1]+=1
            
        if digits[0]==10:
            '''
            there is a carry out, so we need more digits to store the result
            append 0 to the end of array
            and update the first entry to 1
            '''
            digits[0]=1
            digits.append(0)
            
        return digits
      
        
        
    