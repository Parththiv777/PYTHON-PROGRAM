class Solution(object):
    def combinationSum(self, candidates, target):
        # :type candidates: List[int]
        # :type target: int
        # :rtype: List[List[int]]

        stack = []
        for c in candidates:
            if c <= target:
                stack.append([c])
        
        if len(stack) == 0:
            return []

        output = []
        while len(stack) > 0:
            sumlist = stack[-1]
            stack.pop(-1)

            currentsum = 0
            for m in sumlist:
                currentsum = currentsum + m
            
            if currentsum == target:
                output.append(sumlist)
            else:
                for c in candidates:
                    if c >= sumlist[-1]:
                        if currentsum + c < target:
                            variation = list(sumlist)
                            variation.append(c)
                            stack.append(variation)
                        elif currentsum + c == target:
                            variation = list(sumlist)
                            variation.append(c)
                            output.append(variation)

        return output
