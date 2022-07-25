class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        '''- sort the array
           - fix a element and optimize our search for other two elements which is closest to target'''
        num.sort()  #sorting the array
        result = num[0] + num[1] + num[2] #predefine res for reference
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:#here sum is less than target means we have to increase sum value
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result