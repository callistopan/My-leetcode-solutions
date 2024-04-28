class Solution {
public:
    long long minEnd(int n, int x) {
        long long a = x;
        while (--n)
            a = (a + 1) | x;
        return a;
    }
};

/* Example 

n = 3 x = 4
start with x = 4 , for minimum
100
101
110

n = 5 x = 9
start with x = 9 , for minimum
1001
1011           
1101
1111
11001
*/