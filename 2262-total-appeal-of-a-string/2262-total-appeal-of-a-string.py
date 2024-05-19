class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last_pos = [-1] * 26  # Store the last positions of each character
        total_appeal = 0
        current_appeal = 0

        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            current_appeal += i - last_pos[index]
            #print("current appeal "+ str(current_appeal))
            last_pos[index] = i
            total_appeal += current_appeal
            #print("total appeal "+str(total_appeal))

        return total_appeal