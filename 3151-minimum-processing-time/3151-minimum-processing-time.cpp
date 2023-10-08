class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        int n = processorTime.size();
        // sort the tasks
        sort(tasks.begin(), tasks.end());
        sort(processorTime.begin(), processorTime.end());
        reverse(tasks.begin(), tasks.end());

        int maxTime = INT_MIN;


        for ( int i = 0 ; i < 4*n ;i+=4){
            for(int  t = 0 ; t <4 ;t++){
                maxTime = max(maxTime , processorTime[i/4]+ tasks[i+t]);
            }
        }
        return maxTime ;

    }
};