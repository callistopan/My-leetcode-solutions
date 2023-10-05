class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int candidate1=0,candidate2=0;
        int count1=0, count2=0;

        for (int x : nums){
            if (x==candidate1){
                count1++;
            }
            else if (x==candidate2){
                count2++;
            }
            else if (count1==0){
                candidate1=x;
                count1=1;
            }
            else if (count2==0){
                candidate2=x;
                count2=1;
            }
            else{
                count1--;
                count2--;
            }
        }

        count1=0;
        count2=0;
        for (int x :nums){
            if (x==candidate1){
                count1++;
            }
            else if (x== candidate2){
                count2++;
            }
        }

        vector<int> majority;
        if (count1 > nums.size()/3){
            majority.push_back(candidate1);
        }
        if (count2>nums.size()/3){
            majority.push_back(candidate2);
        }
        return majority;
    }
};