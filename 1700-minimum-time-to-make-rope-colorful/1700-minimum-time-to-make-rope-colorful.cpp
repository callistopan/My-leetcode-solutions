class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int n= colors.size();
        int totalTime=0,i=0,j=0;
        
        while (i<n and j<n){
            int currTotal=0,currMax=0;
            
            while (j<n and colors[i]==colors[j]){
                currTotal+=neededTime[j];
                currMax=max(currMax,neededTime[j]);
                j++;
            }
            
            // we needed to delete all except the larger time so that we reduce our cost of removal and satisfy our constraint
            totalTime+= currTotal-currMax;
            i=j;
        }
        return totalTime;
    }
};