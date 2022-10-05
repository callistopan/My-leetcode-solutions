class Solution {
public:
    int maximumSwap(int num) {
        string numstr=to_string(num);
        
        int maxidx=-1, maxdigit=-1;
        int left=-1 , right=-1;
        
        for (int i=numstr.size()-1;i>=0;i--){
            // current digit is larger
            
            if (numstr[i]>maxdigit){
                maxdigit=numstr[i];
                maxidx=i;
                continue;
            }
            
            if (numstr[i]<maxdigit){
                left=i;
                right=maxidx;
            }
        }
        //already inorder
        if (left==-1) return num;
        swap(numstr[left],numstr[right]);
        return stoi(numstr);
        
        
    }
}; 


// 99678 -> 99876
        // 88832188
        // find largest number
        // 2399099