class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string,int> count;
        for (const string& word : words){
            count[word]++;
        }
        
        int answer=0;
        bool central=0;
        
        for (const auto& [word,countOfWord]: count){
            if (word[0]==word[1]){
                if (countOfWord%2==0){
                    answer+=countOfWord;
                }
                else{
                    answer+=countOfWord-1;
                    central=true;
                }
            }
            else if (word[0]<word[1] and count.count({word[1],word[0]})){
                answer+=2*min(countOfWord,count[{word[1],word[0]}]);
            }
        }
        if (central){
            answer++;
        }
        return 2*answer;
    }
};