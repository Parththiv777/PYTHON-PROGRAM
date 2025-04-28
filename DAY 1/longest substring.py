class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        index = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in char_map and char_map[char] >= index:
                index = char_map[char] + 1
            char_map[char] = i
            max_length = max(max_length, i - index + 1)

        return max_length
        
