class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        intervals.extend([newInterval])
        intervals.sort()
        merged=[intervals[0]]
        for i in range(1,len(intervals)):
            if merged[-1][1]>=intervals[i][0]:
                merged[-1][1]=max(merged[-1][1],intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged
