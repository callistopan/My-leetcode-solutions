
public class Solution
{
    public int[] ArrayRankTransform(int[] arr)
    {
        // Store the rank for each number in arr
        Dictionary<int, int> numToRank = new Dictionary<int, int>();
        
        // Deduplicate and sort arr
        int[] sortedNums = new int[arr.Length];
        Array.Copy(arr, sortedNums, arr.Length);
        Array.Sort(sortedNums);
        
        List<int> uniqueNums = new List<int>(sortedNums);
        uniqueNums = uniqueNums.Distinct().ToList();
        
        int rank = 1;
        foreach (int num in uniqueNums)
        {
            numToRank[num] = rank;
            rank++;
        }
        
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = numToRank[arr[i]];
        }
        
        return arr;
    }
}
