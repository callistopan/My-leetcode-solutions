class Solution {
public:
    int minFlips(int a, int b, int c) {
        
        int minimum_flips = 0;

        while (a || b || c){
            int a_bit = a & 1;
            int b_bit = b & 1;
            int c_bit = c & 1;

            if (a_bit && b_bit && !c_bit){

                minimum_flips +=2;
            }
            else if (!a_bit && !b_bit && c_bit){
                minimum_flips += 1;
            }
             else if ((a_bit || b_bit) && !c_bit){
                minimum_flips +=1;
            }
            a >>= 1;
            b >>= 1;
            c >>= 1;


        }
        return minimum_flips;
    }
};