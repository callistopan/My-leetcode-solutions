long long matrixSumQueries(int n, int** queries, int queriesSize, int* queriesColSize){
int done[n][2];
    long long ans = 0;

    for (int i = 0; i < n; i++)
    {
        done[i][0] = 1;
        done[i][1] = 1;
    }
    int cr = 0, cc = 0;

    for (int i = queriesSize - 1; i >= 0; i--)
    {
        if (done[queries[i][1]][queries[i][0]])
        {
            queries[i][0] == 0 ? cr++ : cc++;
            ans += (n - (queries[i][0] == 0 ? cc : cr)) * queries[i][2];
            done[queries[i][1]][queries[i][0]] = 0;
        }
    }
    return ans;
}