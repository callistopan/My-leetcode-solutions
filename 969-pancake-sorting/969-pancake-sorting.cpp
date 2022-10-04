class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> res;
        int flip_length, index;
        
        for (flip_length=arr.size();flip_length>0;--flip_length){
            for(index=0;arr[index]!=flip_length;index++); // finde index to flip
            reverse(arr.begin(),arr.begin()+index+1);
            res.push_back(index+1);
            reverse(arr.begin(),arr.begin()+flip_length); // move to back
            res.push_back(flip_length);
            
        }
        return res;
    }
};