class Solution(object):
    def maxSubArray(self, nums):
        # :type nums: List[int]
        # :rtype: int

        runningsum = nums[0]
        maxsum = nums[0]

        if len(nums) == 1:
            return runningsum

        for i in range(1, len(nums)):
            if nums[i] >= runningsum + nums[i]:
                runningsum = nums[i]
            elif runningsum + nums[i] > nums[i]:
                runningsum = runningsum + nums[i]

            if runningsum > maxsum:
                maxsum = runningsum

        return maxsum
