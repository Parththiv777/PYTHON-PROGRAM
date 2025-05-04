class Solution(object):
    def canJump(self, nums):

        max_reach = 0  

        for i, num in enumerate(nums):

            if i > max_reach:  
                return False

            max_reach = max(max_reach, i + num)  
            
        return True 


sol = Solution()
print(sol.canJump([1, 0, 1, 0]))  
