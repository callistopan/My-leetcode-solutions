class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return '0'
        f=''
        if (numerator<0)^(denominator<0):
            f+='-'
        divident=abs(numerator)
        divisor=abs(denominator)
        
        f+=str(divident//divisor)
        print(f)
        rem=divident%divisor
        print(rem)
        if rem==0:
            return f
        f+='.'
        dic={}
        while rem!=0:
            if rem in dic:
                f=f[:dic[rem]]+'('+f[dic[rem]:]+')'
                break
            dic[rem]=len(f)
            rem*=10
            f+=str(rem//divisor)
            rem=rem%divisor
        return f
        