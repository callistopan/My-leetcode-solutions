class Solution:
    def myPow(self, x: float, y: int) -> float:
        '''if the least significant bit of y is 0, the result is (x^y/2)^2 otherwise, it is x*(x^y/2)^2.
'''
        result, power = 1.0, y
        if y < 0:
            power, x = -power, 1.0/x
        while power:
            if power & 1:
                result *= x
            x *= x
            power >>= 1
        return result
        
    
    
    
    '''
    
    
    
    
    
    
    
    '''