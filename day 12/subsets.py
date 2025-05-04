class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(arr, nums , i ):
            if len(nums) == i:
                res.append(arr[:])
                return
            word = nums[i]
            i+=1   
            backtrack(arr , nums , i)
            arr.append(word)
            backtrack(arr , nums , i)
            arr.pop()
        
        backtrack([] , nums , 0)
        return res
