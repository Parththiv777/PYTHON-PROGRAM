class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0<nums[i]<len(nums)+1 and i+1!= nums[i] and nums[nums[i]-1] != nums[i]:
                t = nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i] = t
        for i in range(len(nums)):
            if i+1!= nums[i]:
                return i+1
        return len(nums)+1
