class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        count = len(nums)
        while i < count:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count -= 1  # One less element to check at the front
            else:
                i += 1
        return nums
