class Solution {
public:
    // O(n*2^n)
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> res;
        for (auto num=1;num<=9;num++){
            dfs(num,n-1,k,res);
        }
        return res;
    }
    
    void dfs(int num,int n,int k,vector<int>& res){
        if (n==0){
            res.push_back(num);
        }
        else{
            int digit = num%10; // last digit 
            if (digit+k<10){
                dfs(num*10+digit+k,n-1,k,res);
            }
            if (k!=0 and digit>=k){
                dfs(num*10+digit-k,n-1,k,res);
            }
        }
    }
};