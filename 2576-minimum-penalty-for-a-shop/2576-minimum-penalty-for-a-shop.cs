public class Solution {
    public int BestClosingTime(string customers) {
        int curPenalty = customers.Count(c => c == 'Y');
        int minPenalty = curPenalty;
        int earliestHour = 0;

        for (int i = 0; i < customers.Length; i++) {
            char ch = customers[i];
            curPenalty += (ch == 'Y') ? -1 : 1;

            if (curPenalty < minPenalty) {
                earliestHour = i + 1;
                minPenalty = curPenalty;
            }
        }
        return earliestHour;
    }
}
