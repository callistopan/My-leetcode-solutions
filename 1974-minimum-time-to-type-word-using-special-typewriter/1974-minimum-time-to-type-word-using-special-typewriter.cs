public class Solution {
    public int MinTimeToType(string word) {
        int n = word.Length;
        int res = n;
        
        for (int i = 0; i < n - 1; i++)
        {
            res += Math.Min(Math.Abs(word[i] - word[i + 1]), 26 - Math.Abs(word[i] - word[i + 1]));
        }
        
        return res + Math.Min(Math.Abs('a' - word[0]), 26 - Math.Abs('a' - word[0]));
    }
}