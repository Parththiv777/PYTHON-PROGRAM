class Solution(object):
    def permute(self, nums):
        # :type nums: List[int]
        # :rtype: List[List[int]]

        stack = []
        for n in nums:
            s = []
            s.append(n)
            stack.append(s)

        output = []
        while len(stack) > 0:
            perm = stack[-1]
            stack.pop(-1)

            if len(perm) == len(nums):
                output.append(perm)
            else:
                used = set(perm)
                for i in range(0, len(nums)):
                    variation = list(perm)
                    if nums[i] not in used:
                        variation.append(nums[i])
                        stack.append(variation)

        return output

        
