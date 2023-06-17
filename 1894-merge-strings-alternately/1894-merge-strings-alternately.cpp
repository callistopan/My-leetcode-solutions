#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string res = "";
        int n = word1.size();
        int m = word2.size();

        int i = 0;

        while (i < n || i < m) {
            if (i < n) {
                res += word1[i];
            }
            if (i < m) {
                res += word2[i];
            }
            i++;
        }
        return res;
    }
};
