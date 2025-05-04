class Solution(object):
    def combine(self, n, k):
        # :type n: int
        # :type k: int
        # :rtype: List[List[int]]

        output = []
        stack = []
        for i in range(1, n + 1):
            stack.append([i])

        while len(stack) > 0:
            combo = stack[-1]
            stack.pop(-1)

            if len(combo) == k:
                output.append(combo)
            else:
                for i in range(combo[-1] + 1, n + 1):
                    variation = list(combo)
                    variation.append(i)
                    stack.append(variation)

        return output



