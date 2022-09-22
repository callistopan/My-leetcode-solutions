class Solution {
public:
    string reverseWords(string s) {
        int lastSpaceIndex=-1;
        int len=(int)s.size();
        
        for (int start=0;start<=len;start++){
            if (start==len or s[start]==' '){
                int l= lastSpaceIndex+1;
                int r=start-1;
                
                while (l<r){
                    char temp= s[l];
                    s[l]=s[r];
                    s[r]=temp;
                    l++;
                    r--;
                }
                lastSpaceIndex=start;
            }
        }
        return s;
    }
};