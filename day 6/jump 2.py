class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump = 0
        i = 0 
        end = 0
        farthest = 0
        final_index = len(nums)-1
        while i < final_index: 
            farthest = max(farthest, nums[i]+i)
            if end == i:
                jump+=1
                end = farthest
                if farthest == final_index:
                    break
            i+=1
        return jump

                
