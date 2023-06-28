class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> ind(n), stack, res;
        for (int i = 0 ; i < n ; i++){
            ind[i] = i;
        }
        // index sorting based on position values
        sort(ind.begin(),ind.end(),[&](int a, int b){
            return positions[a] < positions[b];
        });

        for (int i : ind){ // for positions in increasing order
            if (directions[i] =='R'){ // there is no collisions
                stack.push_back(i);
                continue;
            }
            // current one's directions is 'L' look for 'R's in the stack
            while (!stack.empty() && healths[i] > 0 ){
                // top stack health is less than current one then remove it
                if (healths[stack.back()] < healths[i]){
                    healths[stack.back()] = 0;
                    stack.pop_back();
                    // decrease the health of current one by 1
                    healths[i] --;
                }
                // top stack health is greater than current one, remove current one
                else if (healths[stack.back()] > healths[i]){
                    healths[stack.back()] --;
                    healths[i] = 0;
                }
                else{
                    // same health
                    healths[stack.back()] =0;
                    stack.pop_back();
                    healths[i] = 0;
                }
            }
        }
        // remaining robots
        for (int health : healths){
            if (health > 0){
                res.push_back(health);
            }
        }
        return res;
        


    }
};













