# Initial 2 pointer approach (in case anyone's interested)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]

        i = 0
        j = len(nums)-1
        fi = li = None
        while i<=j:
            if fi is not None and li is not None:
                return [fi, li]
            if fi is None:
                if nums[i] == target:
                    fi = i
                else:
                    i+=1

            if li is None:
                if nums[j] == target:
                    li = j
                else:
                    j-=1

        return [fi, li]
        


# Binary Search approach 
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        li=fi=None
        j=len(nums)-1
        while i <= j:
            mid = i +((j-i)//2)
            if nums[mid] > target:
                j=mid-1
            
            elif nums[mid] < target:
                i = mid+1
            else:
                idx = mid
                while idx>=0 and nums[idx] == target:
                    idx-=1
                fi = idx+1

                idx = mid
                while idx<len(nums) and nums[idx] == target:
                    idx+=1
                li = idx-1 
                break

        if fi is None and li is None:
            return [-1, -1]
        return [fi, li]
