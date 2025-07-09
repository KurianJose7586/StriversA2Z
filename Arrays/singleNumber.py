from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
       d = defaultdict(lambda: 2)
       for i in nums:
        d[i] -= 1
       
       for i in d:
        if d[i] !=0 :
            return i

    
        
