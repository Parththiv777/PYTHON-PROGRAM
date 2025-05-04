class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        max_index = 0
        max_value = 0
        for i in range(n):
            if height[i] > max_value:
                max_index = i
                max_value = height[i]
        left_max_index = 0
        left_max = 0
        water = 0
        for i in range(max_index):
            if height[i] > left_max:
                left_max_index = i
                left_max = height[i]
            else:
                water += left_max - height[i]
        right_max_index = 0
        right_max = 0
        for i in range(n - 1, max_index, -1):
            if height[i] > right_max:
                right_max_index = i
                right_max = height[i]
            else:
                water += right_max - height[i]
        return water
