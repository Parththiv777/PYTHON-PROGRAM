class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        combination = []
        self.backtrack(candidates, target, 0, combination, result)
        return result

    def backtrack(self, candidates, target, start, combination, result):
        if target == 0:
            result.append(list(combination))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue  # skip duplicates
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, combination, result)
            combination.pop()
