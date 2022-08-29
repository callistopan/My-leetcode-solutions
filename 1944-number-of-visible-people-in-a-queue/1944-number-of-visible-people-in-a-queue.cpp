class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        
        vector<int> res(heights.size(),0);
        stack<int> s;
        
        for (int i=0;i<heights.size();i++){
            
            while (!s.empty() and heights[s.top()] <=heights[i]){
                res[s.top()]++;
                s.pop();
            }
            if (!s.empty()){
                res[s.top()]++;
            }
            s.push(i);
        }
        return res;
        
        
    }
};


    /*
    '''
    res = 3 1 2 1 0 0
    10 -stack=0
    6  - stack[-1]=0   stack=0 1
    8  - stack=0 2 stack[-1]=0 
    5  - stack=0 2 3
    11 - stack= empty
    9  - nothing
    
    
    '''
    */