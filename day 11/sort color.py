class Solution(object):
    def sortColors(self, nums):
        left = 0
        middle = 0
        right = len(nums) - 1
        
        red = 0
        white = 1
        blue = 2
        
        while middle <= right:
            if nums[middle] == red:
                nums[middle], nums[left] = nums[left], nums[middle]
                middle += 1
                left += 1
            elif nums[middle] == white:
                middle += 1
            elif nums[middle] == blue:
                nums[middle], nums[right] =  nums[right], nums[middle]
                right -= 1
        
