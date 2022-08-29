class Solution {
public:
    //We convert num to a string and then:

// If negative: sort descending, excluding the sign.
// If positive: sort ascending
// Find first non-zero number (e.g. 000237)
// Swap it with the first number (e.g. 200037)
    
    long long smallestNumber(long long num) {
        
        auto s = to_string(abs(num));
        sort(begin(s),end(s),[&](int a,int b){return num<0? a>b:a<b;});
        if (num>0){
            swap(s[0],s[s.find_first_not_of('0')]); //  find first occurence of none zero
            
        }
        return stoll(s)*(num<0 ?-1:1);  // stoll used for converting string into long long
        
    }
};