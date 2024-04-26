int numberOfBeams(char** bank, int bankSize) {
    int prev = 0, ans = 0;
    for (int i = 0; i < bankSize; i++) {
        int count = 0;
        
        while (*bank[i] != '\0') { // Use a different pointer for iteration
            if (*bank[i] == '1') {
                count++;
            }
            bank[i]++; // Move to the next character
        }
        if (count != 0) {
            ans += (prev * count); // Add count to the previous count
            prev = count;
        }
    }
    return ans;
}