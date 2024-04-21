int numberOfSpecialChars(char* word) {
    bool lowercase[26] = {false};
    bool uppercase[26] = {false};
    bool flag[26] ={false};
    int count = 0;

    for (int i = 0; word[i] != '\0'; i++) {
        char c = word[i];
        if (isalpha(c)) {
            if (islower(c)) {
                
                    if(i>0 && uppercase[c-'a']){
                        flag[c-'a'] = true;
                    }
                    lowercase[c - 'a'] = true;
                
            } else {
                
                    uppercase[c - 'A'] = true;
                
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        if (lowercase[i] && uppercase[i] && !flag[i]) {
            count++;
        }
    }

    return count;
}