class Solution {
public:
    int vis[100005];
    int medianOfUniquenessArray(vector<int>& nums) {
        long long tot=nums.size();
        tot=(tot+1)*tot/2; // total sub arrays
        long long need=(tot-1)/2;
      printf("%lld\n",need);
        int Max=nums.size()+1,Min=0;
        for(auto it:nums)vis[it]=0;
        //  ATMOST MID UNIQUE ELEMENTS
        while(Max>Min+1){
            int mid=(Max+Min)/2;
            int l=0,cnt=0;
            long long sum=0; // SUM OF DISTINCT NUMBER OF SUB ARRAYS
            for(int i = 0;i<nums.size();i++){
                if(!vis[nums[i]])cnt++;
                vis[nums[i]]++;
                while(cnt>=mid){
                    vis[nums[l]]--;
                    if(vis[nums[l]]==0)cnt--;
                    l++;
                }
                sum+=i-l+1;
            }
               for(auto it:nums)vis[it]=0;
            printf("%d %d\n",mid,sum);
            if(sum<=need)Min=mid;
            else Max=mid;
        }
        return Min;
    }
};

/* run
need =7
3 12 
1 0
2 5

vis
{ 3:0,4:2,5:1}
[3,4,3,4,5]

[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]

Max = 6 min = 0
Mid = 3
l= 2 count = 2 sum = 10 */














