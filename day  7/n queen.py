class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                # Check if placing the queen at (p, q) is safe
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    # Recurse with updated lists (place the queen and continue)
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []  # To store all solutions
        DFS([], [], [])  # Start DFS with an empty board (no queens placed)

        # Format the solutions as boards
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


# Example usage:
param_1 = 4
ret = Solution().solveNQueens(param_1)

# Print the result
for solution in ret:
    for row in solution:
        print(row)
    print()
