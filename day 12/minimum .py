class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        left = 0
        right = 0
        string_to_count, initial_visited = self.build_visited_and_count(t)
        min_string = (m + 1) * "a"
        visited = initial_visited.copy()
        current_string = ""
        reset = False
        while left < m - n + 1:
            if s[left] not in string_to_count.keys():
                left += 1
                if len(current_string) > 1:
                    current_string = current_string[1:]
                if right < left:
                    right = left
            elif right != m and not reset:
                if s[right] in string_to_count.keys():
                    visited[s[right]] += 1
                current_string += s[right]
                right += 1
            reset = False
            if self.compare(string_to_count, visited):
                if len(current_string) < len(min_string):
                    min_string = current_string
                if s[left] in visited.keys():
                    visited[s[left]] -= 1
                left += 1
                current_string = current_string[1:]
                reset = True
            elif right == m:
                break
        if len(min_string) == m + 1:
            return ""
        return min_string
    
    def compare(self, count, visited):
        for key in count.keys():
            if visited[key] < count[key]:
                return False
        return True

    
    def build_visited_and_count(self, t):
        count = {}
        visited = {}
        for i in range(len(t)):
            count[t[i]] = count.get(t[i], 0) + 1
            visited[t[i]] = 0
        return count, visited
        
