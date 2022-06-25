class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''1. create a dictionary ,key as the number and value as the possible alphabets
           2. select a string according to the input string
           3. then backtrack for next index
           4. if index ever reaches the length of our input string then we need to return and we found a possible path'''
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index ==len(nums):
            res.append(path)
            return
            
        string1 =dic[nums[index]]
        for i in string1:   #for every character in the string
            self.dfs(nums, index+1, dic, path + i, res)  #backtrack