class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid #returns the index where the target is found
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left #returning the left index if the given target isn't in the list and this is going to be the index at which the target would have been placed if it was in the list.
