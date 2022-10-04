bool cmp(vector<int>& a,vector<int>& b) {return a[1]<b[1];} // sort by end
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& segments) {
        //sort by end
        sort(segments.begin(),segments.end(),cmp);
        int ans=0;
        int current_arrow=0;
        for (int i=0;i<segments.size();i++){
            if (ans==0 or segments[i][0]>current_arrow){
                ans++;
                current_arrow=segments[i][1];// update the arrow 
            }
        }
        
        return ans;
        
    }
};