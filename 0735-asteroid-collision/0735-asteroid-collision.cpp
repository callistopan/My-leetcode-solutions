class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;

        for (int asteroid : asteroids){
            int flag = 1;
            while (!st.empty() && (st.top() > 0 && asteroid < 0)){ // -> <- collision condition

                // top is smaller then explode it
                if (abs(st.top()) < abs(asteroid)){
                    st.pop();
                    continue;
                }

                // same size explode both
                else if (abs(st.top()) == abs(asteroid)){
                    st.pop();
                }

                // current asteroid is destroyed
                flag = 0;
                break;
            }

            if (flag){ // not destroyed yet
                st.push(asteroid);
            }
        }

        // return remaining asteroids
        vector<int> remainingAsteroids (st.size());
        for (int i = remainingAsteroids.size()-1; i>=0;i--){
            remainingAsteroids[i] = st.top();
            st.pop();
        }
        return remainingAsteroids;

    }
};









