class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        counter = 0
        maxLen = 0
        for num in nums:
            if num == 1:
                counter += 1
                maxLen = max(maxLen, counter)
            else:
                counter = 0
        return maxLen

        
