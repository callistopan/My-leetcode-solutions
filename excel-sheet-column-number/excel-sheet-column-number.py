class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        reverse = columnTitle[::-1]
        i = 0
        columnNumber = 0
        while i<len(columnTitle):
            columnNumber += (26**i)*(ord(reverse[i]) - 65 + 1)
            i+=1
        return columnNumber