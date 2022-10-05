class Solution {
public:
    int maxDistance(vector<int>& colors) {
        
        int res=0;
        int n=colors.size();
        int l=0,r=n-1;
        
        while (r>=0 and colors[0]==colors[r]) r--;
        res=max(res,r);
        while (l<n and colors[n-1]==colors[l])l++;
        res=max(res,n-l-1);
        
        return res;
    }
};