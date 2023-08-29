public class Solution {
    public int BestClosingTime(string customers) {
        // start with closing at hour 0 , the penalty is all 'Y' in closed hours
        int curPenalty = customers.Count(c => c=='Y');
        int minPenalty = curPenalty;

        int earliestHour = 0;

        for (int i = 0 ; i < customers.Length; i++){
            char ch = customers[i];
            if (ch == 'Y'){
                curPenalty --;
            }
            else{
                curPenalty ++;
            }

            if (curPenalty < minPenalty){
                earliestHour  = i +1;
                minPenalty = curPenalty;
            }
        }
        return earliestHour;

        
    }
}