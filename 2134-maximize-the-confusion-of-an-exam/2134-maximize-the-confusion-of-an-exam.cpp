class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int res = 0;
        int n = answerKey.size();
        int l = 0 , r = 0 , t = 0 , f = 0; // true and false

        while (r < n ){
            if (answerKey[r]=='T'){
                t++;
            }
            else{
                f++;
            }
            while ( min(t,f) > k){ // cant change one of the character to other
                if(answerKey[l]=='T'){
                    t--;      
                }
                else{
                    f--;
                }
                l++;
            }

            res = max(res, r-l+1);
            r++;
        }
        return res;

    }
};