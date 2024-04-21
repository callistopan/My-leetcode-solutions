int minTimeToType(char* word) {
    int n = strlen(word);
    int res = n;
    for(int i = 0;i < n - 1;i++){
        res += fmin(abs(word[i] - word[i+1]) , 26 - abs(word[i] - word[i+1]));
    }
    return res + fmin(abs((int) 'a' - word[0]), 26 - abs((int) 'a' - word[0]));
}