public class Solution {
    public int MinimumPushes(string word) {
        int[] letterCounts = new int[26];
        foreach (char c in word){
            letterCounts[c-'a']++;
        }

        int[] sortedCounts = letterCounts.OrderByDescending(x => x).ToArray();
        int totalKeyPresses = 0;
        for (int index = 0; index < sortedCounts.Length; index++){
            int count = sortedCounts[index];
            if (count == 0)
                break;
            totalKeyPresses += (index/8 + 1) * count; 
        }
        return totalKeyPresses;
    }
}

/*
Main Idea:
Sort the characters based on their frequency
Completely place the top 8 characters at first place.
After that try to placed the remaining in second place and so on.
This method would ensure that we are doing the minimum number of operations here


*/
