int numberOfSpecialChars(char* word) {
    bool lowercase[26] = {false};
    bool uppercase[26] = {false};
    int count = 0;

    for (int i = 0; word[i] != '\0'; i++) {
        char c = word[i];
        if (isalpha(c)) {
            if (islower(c)) {
                if (!lowercase[c - 'a']) {
                    lowercase[c - 'a'] = true;
                }
            } else {
                if (!uppercase[c - 'A']) {
                    uppercase[c - 'A'] = true;
                }
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        if (lowercase[i] && uppercase[i]) {
            count++;
        }
    }

    return count;
}